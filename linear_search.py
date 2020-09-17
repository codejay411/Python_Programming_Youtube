def linear(ram,x):
    for i in range(len(ram)):
        if ram[i]==x:
            return i
    return -1

ram=[1,3,5,7,8,76,754,34,2,321,1223,546,78,89,9,970]
x=3424
a=linear(ram,x)
if(a==-1):
    print("Element is not found in the list")
else:
    print("Element found at index ",a)



