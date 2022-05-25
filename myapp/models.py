from django.db import models

# Create your models here.

from datetime import datetime
from django.utils import timezone
# Create your models here.

class user_detail(models.Model):
	name=models.CharField(max_length=30)
	username=models.CharField(max_length=30,unique=False)
	email=models.CharField(max_length=30,unique=True)
	password=models.CharField(max_length=30)
	date = models.DateTimeField(default=timezone.now, editable=False)
	organization=models.CharField(max_length=30)
	privilege=models.CharField(max_length=30)
	class Meta:
		db_table="user_detail"


class dev_data(models.Model):
	#owner =models.CharField(max_length=40,null=True) 
	devid=models.TextField()
	voltage=models.TextField(null=True)
	active_power_W=models.TextField(null=True)
	apparent_power_VA=models.TextField(null=True)
	active_energy_Wh=models.TextField(null=True)
	apparent_energy_VAh=models.TextField(null=True)
	phase_current=models.TextField(null=True)
	neutral_current=models.TextField(null=True)
	frequency=models.TextField(null=True)
	pf=models.TextField(null=True)
	meter_time=models.TextField(null=True)
	date = models.DateTimeField(default=timezone.now, editable=False)
	class Meta:
		db_table="dev_data"

	def get_date(self):
		time = datetime.now()
		print(time)
		if self.date.day == time.day:
		    if str(time.hour - self.date.hour)<=1:
		    	return "Live"
		else:
		    if self.date.month == time.month:
		        return "Down"#str(time.day - self.date.day) + " days ago"
		    else:
		        if self.date.year == time.year:
		            return "Down"#str(time.month - self.date.month) + " months ago"
		return "Down"#self.date