num=int(input("Enter the number : "))

c=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(c, end="")
        c=c+1
    print("")