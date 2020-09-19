def binary(list1, x):
    first=0
    last=len(list1)-1
    mid=0
    while(first<=last):
        mid=(first+last)//2
        if(x>list1[mid]):
            first=mid+1
        elif(x<list1[mid]):
            last=mid-1
        else:
            return mid
    else:
        return -1

list1 = [3, 5, 7, 8, 9, 13, 34, 87, 88, 98, 99, 132, 143, 176, 234, 567, 876, 9876]
x=87

r=binary(list1, x)
if(r==-1):
    print("Elemene are not found")
else:
    print("element are found at position ", r)