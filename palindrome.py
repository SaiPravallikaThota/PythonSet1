NUM=int(input("Enter number:"))
T=NUM
REV=0
while(NUM>0):
    a=NUM%10
    REV=REV*10+a
    NUM=NUM//10
if(T==REV):
    print("yes")
else:
    print("no")
