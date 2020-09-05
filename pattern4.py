num=int(input("enter the number of rows: "))
c=1
for i in range(1,num+1):
    for j in range(1,num-i+2):
        print(c,"  ",end='')
        c=c+1
    print()

    