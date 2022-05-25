

function mtype_change() {
 console.log("mtype is calling");
  var mtype=document.getElementById("mtype").value
  var url = "{% url 'mtype_update' %}";        
  window.location.href = '/mtypeupdate/?mtype='+mtype; // alert(mtype);


  // var content=document.getElementById("cc").value
  //alert(parentid)
        //   $.ajax({
        //     type: 'POST',       // define the type of HTTP verb we want to use (POST for our form)
        //     url: '/mtypeupdate/',
        //     dataType: 'json',
        //     data: JSON.stringify({
        //     'mtype': mtype,
        //     'parentid':'121'
        //            }), 
        //     success: function (json) {
        //          var url = "{% url 'mtype_update' %}";
        //           document.location.href = url;
        //         //window.location.reload();
        //   //       if (json.length < 1 || json == undefined) {
                   
        //   //   //empty
        //   // }
        //   // alert(json['mid'])
        //   //     document.getElementById("commandsub1").value = json['mid'];
        //   //      document.getElementById("commandsub2").value = json['fc'];
        //   //       document.getElementById("commandsub3").value = json['address'];
        //   //        document.getElementById("commandsub4").value = json['data'];
        //   //         document.getElementById("commandsub5").value = json['crc']
        //   //         document.getElementById("commandsub5").value = json['crc']
        //     },
        //     error: function (exception) {
        //         alert('Exeption:' + exception);
        //     },
        // });
  
  }



