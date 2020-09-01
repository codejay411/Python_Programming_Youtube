num=int(input("Enter the number : "))
p=len(str(num))

# check armstrong number
temp=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem**p
    num=num//10
if(temp==sum):
    print("Number is armstrong number ")
else:
    print("Number is not armstrong")