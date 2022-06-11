a,b,c,d,e,f,x = map(int,input().split())

aoki = 0
takahashi = 0

set_t = x // (a + c) 
set_a = x // (d + f)
nokori_t = x - set_t * (a + c)
nokori_a = x - set_a * (d + f)

if (nokori_t >= a):
    nokori_t = a
if (nokori_a >= d):
    nokori_a = d

takahashi = (set_t * a + nokori_t) * b 
aoki = (set_a * d + nokori_a) * e

if (aoki > takahashi):
    print("Aoki")
elif(aoki < takahashi):
    print("Takahashi")
else:
    print("Draw")

