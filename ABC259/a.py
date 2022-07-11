n,m,x,t,d = map(int,input().split())

if x-m <= 0:
    print(t)
else:
    print(t - d *(x-m))