low = int(input("Enter lower range: "))  
upp = int(input("Enter upper range: "))  
for n in range(low+1,upp):  
   if n > 1:  
       for i in range(2,n):  
           if (n % i) == 0:  
               break  
       else:  
           print(n)  
