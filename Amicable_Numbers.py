def get_pfs(num):  # n = 10
    s=0
    for i in range(1, num):
        if num%i==0:
            s+=i
    return s #8
a=int(input())
b=int(input())
if get_pfs(a)==b and get_pfs(b)==a: #get_pfs(10)
    print('Amicable')
else:
    print('Not Amicable')
