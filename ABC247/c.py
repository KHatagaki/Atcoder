n = int(input())

list = []

s_list = []
s_list.append("1")
for i in range(2,n+1):
    s_list.append(str(s_list[i-2]) + " " + str(i) + " " + str(s_list[i-2]))
print(s_list[n-1])