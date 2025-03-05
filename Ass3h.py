n=int(input())
temp=n
s=0
while temp>0:
    r=temp%10
    s+=r**3
    temp//=10

if s==n:
    print('Armstrong')
else:
    print('Not Armstrong')