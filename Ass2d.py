def relational(a,b):
    if a<b:
        print('a is less than b')
    elif a<=b:
        print('a is less than or equal to b')
    elif a>b:
        print('a is greater than b')
    elif a>=b:
        print('a is greater than or equal to b')
    else:
        print('Other operator')

a=int(input())
b=int(input())
print(relational(a,b))