def find_index(arr, value):
    try:
        return arr.index(value)
    except ValueError:
        return -1  

arr=list(map(int,input().split()))
value = int(input())
print(find_index(arr, value))
