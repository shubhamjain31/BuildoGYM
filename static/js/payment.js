function validatePayment(){
var name=document.myform.inputName.value;
var month=document.myform.inputMonth.value;
var date=document.myform.inputDate.value;
var amount=document.myform.inputAmount.value;
var message=document.myform.message.value;
if (name=="Select Name"){  
          alert("Please select the name value"); 
        return false;  
        }
if (month=="Select Month"){  
          alert("Please select the month value"); 
        return false;  
        }
if (date==null || date==""){  
          alert("Date field is empty"); 
        return false;  
        }
if (amount==null || amount==""){  
          alert("Amount field is empty"); 
        return false;  
}     
if (message==null || message==""){  
          alert("Message field is empty"); 
        return false;  
}
}