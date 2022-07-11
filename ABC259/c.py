s = input()
t = input()

to_s = list(s[0])
to_s.append("1") 
to_t = list(t[0])
to_t.append("1")
idx = 1

for i in range(len(s)):
    if i == 0:
        continue
    if s[i-1] == s[i]:
        to_s[idx] = str(int(to_s[idx]) + 1)
    else:
        to_s.append(s[i])
        to_s.append("1")
        idx += 2

idx = 1
for i in range(len(t)):
    if i == 0:
        continue
    if t[i-1] == t[i]:
        to_t[idx] = str(int(to_t[idx]) + 1)
    else:
        to_t.append(t[i])
        to_t.append("1")
        idx += 2

if (len(to_t) != len(to_s)):
    print("No")
    exit()


for i in range(0,len(to_t),2):
    if to_t[i] != to_s[i]:
        print("No")
        exit()
    elif to_s[i+1] == "1" and to_t[i+1] != "1":
        print("No")
        exit()
    elif int(to_s[i+1]) > int(to_t[i+1]):
        print("No")
        exit()

print("Yes")
        