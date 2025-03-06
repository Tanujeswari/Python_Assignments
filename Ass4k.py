arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print("Common values are:",*set(arr1).intersection(arr2))