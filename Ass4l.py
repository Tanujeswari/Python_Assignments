arr1 = list(map(int,input().split()))
arr2 = [] 
for i in arr1:
    if i not in arr2:
        arr2.append(i)
print(*arr2)