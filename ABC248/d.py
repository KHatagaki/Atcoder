from collections import Counter

n = int(input())

a = list(map(int,input().split()))

q = int(input())
cnt = []
for i in range(n):
    cnt.append(Counter(a[:i+1]))

result = []
for i in range(q):
    l_q,r_q,x_q = map(int,input().split())
    if l_q == 1:
        result.append(int(cnt[r_q-1].get(x_q,"0")))
    elif l_q == r_q:
        result.append(int(cnt[r_q].get(x_q,"0")) - int(cnt[r_q-1].get(x_q,"0")))
    else:
        result.append(int(cnt[r_q-1].get(x_q,"0")) - int(cnt[l_q-1].get(x_q,"0")))

for i in result:
    print(i)
