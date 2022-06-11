n = input()

list = list(map(int,input().split()))

list.sort(reverse=True)
score = 0
cnt = 0
for i in list:
    if cnt % 2 == 0:
        score += i
    else:
        score -= i
    cnt += 1

print(score)