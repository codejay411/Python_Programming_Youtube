num=int(input("enter the number : "))
for i in range(0,num):
    for j in range(num-1,i,-1):
        print(j," ",end='')
    for l in range(i):
        print("      ",end='')
    for k in range(i+1,num):
        print(k," ",end='')
    print("")