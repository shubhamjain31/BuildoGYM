function validateShift(){
var title=document.myform.title.value;
var sfrom=document.myform.shiftFrom.value;
var sto=document.myform.shiftTo.value;
var message=document.myform.message.value;

if (title==null || title==""){  
          alert("Title field is empty"); 
        return false;  
        }
if (sfrom==null || sfrom==""){  
          alert("Shift From time field is empty"); 
        return false;  
        }
if (sto==null || sto==""){  
          alert("Shift To time field is empty"); 
        return false;  
        }
if (message==null || message==""){  
          alert("Message field is empty"); 
        return false;  
} 
}