def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)

num=int(input("Enter the number : "))
if(num<0):
    print("factorial are not found of negative number ")
elif(num==0):
    print("factorila of 0 is 1")
else:
    print('factorial of',num,'is',fact(num))

