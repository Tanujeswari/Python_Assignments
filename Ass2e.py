def greater(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return a,b
a=int(input())
b=int(input())
print(greater(a,b))

'''
def greater(a,b):
    if a>b:
        print('a is big and b is small')
    elif a<b:
        print('a is small and b is big')
    else:
        print('Both are equal')
a=int(input())
b=int(input())
print(greater(a,b))

'''