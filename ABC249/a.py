a,b,c,d,e,f,x = map(int,input().split())

aoki = 0
takahashi = 0

for i in range(1,x+1):
    if (i % (a+c+1) <= a):
        takahashi += b
    if(i % (d+f+1) <= d):
        aoki += e
if (aoki > takahashi):
    print("Aoki")
elif(aoki < takahashi):
    print("Takahashi")
else:
    print("Draw")

