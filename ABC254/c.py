n, k = map(int,input().split())

a = list(map(int,input().split()))
swap = []
flag = True
temp = []

for i in range(k):
    list_v = a[i::k]
    list_v.sort()
    swap.append(list_v)

for i in range(-1*(-n//k)):
    if(i != -1*(-n//k)-1):
        check = [x[i] for x in swap]
        temp = list(check)
        check.sort()
        if temp != check:
            flag = False
            break
    else:
        for j in range(k):
            if(len(swap[j])==-1*(-n//k)):
                check.append(swap[j][i])
            else:
                break
        temp = list(check)
        check.sort()
        if temp != check:
            flag = False
    check = []

if(flag == False):
    print("No")
else:
    print("Yes")