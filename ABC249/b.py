s = input()
flag = True
if (s.islower() == True or s.isupper() == True):
    print("No")
    exit()

for i in range(len(s)):
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            flag = False
            break
    if flag == False:
        break

if (flag == True):
    print("Yes")
else:
    print("No")