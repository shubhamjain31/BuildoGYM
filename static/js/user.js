function validateUser(){
var fname=document.myform.inputFname.value;
var lname=document.myform.inputLname.value;
var email=document.myform.inputEmail4.value;
var package=document.myform.package.value;
var shift=document.myform.inputShift.value;
var password=document.myform.inputPassword4.value;
var phone=document.myform.inputMobile.value;
var address=document.myform.inputAddress.value;
var city=document.myform.inputCity
.value;
var gender=document.myform.inputGender.value;
var zip=document.myform.inputZip.value;
if (fname==null || fname==""){  
          alert("First Name field is empty"); 
        return false;  
        }
if (lname==null || lname==""){  
          alert("Last Name field is empty"); 
        return false;  
        }
if (package=="Choose Package"){  
          alert("Please select the package value"); 
        return false;  
        }
if (shift=="Choose Shift"){  
          alert("Please select the shift value"); 
        return false;  
        }
if (email==null || email==""){  
          alert("Email field is empty"); 
        return false;  
        }
if (password==null || password==""){  
          alert("Password field is empty"); 
        return false;  
}     
if (phone==null || phone==""){  
          alert("Mobile field is empty"); 
        return false;  
}

if (address==null || address==""){  
          alert("Address field is empty"); 
        return false;  
}
if (city==null || city==""){  
          alert("City field is empty"); 
        return false;  
}
if (gender=="Select Gender"){  
          alert("Please select the gender value"); 
        return false;  
        }
if (zip==null || zip==""){  
          alert("Zip field is empty"); 
        return false;  
}
}