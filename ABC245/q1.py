a,b,c,d =map(int, input().split())

takahashi = 3600 * a + 60 * b
aoki = 3600 * c + 60 * d + 1
if(takahashi > aoki):
    print("Aoki")
else:
    print("Takahashi")
