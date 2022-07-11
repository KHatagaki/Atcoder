n,q = map(int,input().split())
s = input() 
query = []
p=0

for i in range(q):
    t,x = map(int,input().split())
    if t == 1:
        p += x
        p %= n
    else:
        print(s[(x-1-p)%n])
