def remove_element(arr, value):
    if value in arr:
        arr.remove(value)
    return arr

'''
arr=list(map(int,input().split()))
value=int(input())
print(*remove_element(arr, value))
'''