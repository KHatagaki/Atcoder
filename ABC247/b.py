n = int(input())

s = []
t = []

for i in range(n):
    s_,t_ = map(str,input().split())
    s.append(s_)
    t.append(t_)

check_list = []
for s_n,t_n in zip(s,t):
    if(s_n == t_n):
        continue
    if s.count(s_n) + t.count(s_n) > 1:
        check_list.append(s_n)
    if s.count(t_n) + t.count(t_n) > 1:
        check_list.append(t_n)
check_list = set(check_list)
check_list = list(check_list)
for s_n,t_n in zip(s,t):
    if s_n in check_list and t_n in check_list:
        print("No")
        exit()
print("Yes")


