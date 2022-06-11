n = input()
list = []

for i in range(0,int(n)):
    list.append(int(input()))

list.sort()
result = []
for i in list:
    if i not in result:
        result.append(i)
print(len(result))