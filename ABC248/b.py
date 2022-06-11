a,b,k = map(int,input().split())
cnt = 0
while True:
    if a >= b:
        break
    a *= k
    cnt += 1

print(cnt)
