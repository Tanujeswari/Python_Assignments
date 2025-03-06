arr = list(map(int,input().split()))

minposition = arr.index(min(arr))
print ("The minimum is at position:", minposition)

maxposition = arr.index(max(arr))
print ("The maximum is at position::", maxposition)