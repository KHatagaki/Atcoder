s = input()
list = ["dream","dreamer","erase","eraser"]
index = 0
flag = False
s += "$$$"
str = ""
while index <= len(s) + 2:
    print(index)
    print(str+"$$",s)
    if str + "$$" == s:
        flag = True
        break
    if s[index] == 'a' or s[index] == '$':
        index -= 2
        str = str[:-2]
    elif s[index] == 'd':
        if s[index + 6] != '$': 
            str += list[1]
            index += 7
        else:
            str += list[0]
            index += 5
    elif s[index] == 'e':
        if s[index + 4] == "r":
            str += list[3]
            index += 6
        else:
            str += list[2]
            index += 5
    else:
        break

if flag == True:
    print("YES")
else:
    print("NO")
