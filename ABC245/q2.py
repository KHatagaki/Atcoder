n = int(input())

a = list(map(int,input().split()))

b=0

while True:
    if b in a:
        b += 1
        continue
    else:
        break
print(b)