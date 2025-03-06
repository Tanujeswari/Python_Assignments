arr1=list(map(int,input().split()))
e_count = 0
o_count= 0
for i in arr1:
    if i % 2 == 0:
        e_count += 1
    else:
        o_count += 1 
print("Even Numbers in given array:",e_count)
print("Odd Numbers in given array:",o_count)