from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os, signal
import time
import psycopg2
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib import messages
import json 
from django.shortcuts import redirect
from .models import user_detail,dev_data
from django.db.models import Q
from django.contrib.auth import logout
# Create your views here.

@csrf_exempt
def login(request): 
	return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')
@csrf_exempt
def load(request):
	print('hello',request.method)
	# Ask user for the name of process
	name = "postgres"#"client.py" ##input("Enter process Name: ")
	try:
		
		# iterating through each instance of the process
		for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
			print(line)
			fields = line.split()
			
			# extracting Process ID from the output
			pid = fields[0]
			print('process id is:',pid)
			# terminating process
			#os.kill(int(pid), signal.SIGKILL)
			os.system("sudo kill -9 "+pid)
		print("Process Successfully terminated")
		time.sleep(3)
		os.system('systemctl restart postgresql')
		time.sleep(3)
		conn = psycopg2.connect(
   				database="chirpstack_ns", user='postgres', password='dbpassword', host='localhost', port= '5432')	
		#Creating a cursor object using the cursor() method
		c = conn.cursor()

		#Executing an MYSQL function using the execute() method
		c.execute("select version()")
		c.execute("TRUNCATE TABLE device_queue")
		# Fetch a single row using fetchone() method.
		#data = c.fetchone()
		#print("Connection established to: ",data)
		# Close the connection
		conn.commit()
		conn.close()
		print('device device_queue cleared')
	except Exception as e:
		print("Error Encountered while running script",e)
	#messages.info(request, 'Your password has been changed successfully!')
	t='yes'
	return render(request, 'index.html',{'t':t})

@csrf_exempt
def mqtt_test(request):
	if request.method == 'POST':
	    data = request.body.decode('utf-8')
	    json_data = json.loads(data)
	    #print(json_data)
	    dev_id=json_data['data']
	    mdev=json.loads(dev_id)
	    post=dev_data()
	    post.devid=mdev['meter_address']
	    post.voltage=mdev['voltage']
	    post.active_power_W=mdev['active_power_W']
	    post.apparent_power_VA=mdev['apparent_power_VA']
	    post.active_energy_Wh=mdev['active_energy_Wh']
	    post.apparent_energy_VAh=mdev['apparent_energy_VAh']
	    post.phase_current=mdev['phase_current']
	    post.neutral_current=mdev['neutral_current']
	    post.frequency=mdev['frequency']
	    post.pf=mdev['PF']
	    post.meter_time=mdev['meter_time']
	    post.save()
	    return HttpResponse("okkkk POST it")
	return HttpResponse("hello i get GET Request")

@csrf_exempt
def meterlist(request): 
		p=user_detail.objects.get(email=request.session.get('semail'))
		all_user=dev_data.objects.all()[:20]
		return render(request, 'meterlist.html',{'row':p,'all_user':all_user})
		return render(request, 'login.html')

@csrf_exempt
def signin(request):
	if request.POST.get('username') or request.POST.get('email'):
		try:
			p=user_detail.objects.get(Q(email=request.POST.get('email')) & Q(password=request.POST.get('password')))
			request.session['semail'] =request.POST.get('email') 
			return redirect('meterlist')
		except:
			print("exception on site login")
			messages.success(request, "Wrong Email or Password!")
			return redirect('meterlist')

@csrf_exempt
def register(request): 
	return render(request, 'register.html')

@csrf_exempt
def home(request):
	post=user_detail()
	post.username= 'dummy'#request.POST.get('username')
	post.email= 'ok@gmail.com'#request.POST.get('email')
	post.password= '123' #request.POST.get('password')
	post.save()	
	request.session['semail'] ='ok@gmail.com'			
	#p=user_detail.objects.get(email=request.POST.get('semail')) 
	return HttpResponse('ok up') 



@csrf_exempt
def edit_meter_read(request,mtype): 
	devid=mtype
	print('***** meter type as ******',mtype)
	p=user_detail.objects.get(email=request.session.get('semail'))
	if p:
		result2 =dev_data.objects.filter(devid=devid)[:100]
		print(result2)
		return render(request, 'meteraddwrite_edit.html',{'row':p,'meter_list':result2})
	else:
		print("**Not Read Meter Created**")
		return redirect('meterlist')
	conn.close()