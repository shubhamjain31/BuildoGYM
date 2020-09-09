function validatePackage(){
var title=document.myform.title.value;
var fee=document.myform.fee.value;
var message=document.myform.message.value;

if (title==null || title==""){  
          alert("Title field is empty"); 
        return false;  
        }
if (fee==null || fee==""){  
          alert("Fee field is empty"); 
        return false;  
        }
if (message==null || message==""){  
          alert("Message field is empty"); 
        return false;  
} 
}