Digit= int(input("Enter a number: "))  
if Digit > 1:  
   for i in range(2,Digit):  
       if (Digit % i) == 0:  
           print("no")  
           break  
   else:  
       print("yes")  
         
else:  
   print("no") 
