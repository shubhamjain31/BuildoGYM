function validateAttendance(){
var name=document.myform.inputName.value;
var date=document.myform.inputDate.value;
var message=document.myform.message.value;
if (name=="Select Name"){  
          alert("Please select the name value"); 
        return false;  
        }
if (date==null || date==""){  
          alert("Date field is empty"); 
        return false;  
        } 
if (message==null || message==""){  
          alert("Message field is empty"); 
        return false;  
}
}