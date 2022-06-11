n,k =map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
idx = []
max_d = max(a)

for i in range(len(a)):
    if(max_d == a[i]):
        idx.append(i)
#print(idx)

for i in b:
    if(i-1 in idx):
        print("Yes")
        exit()
print("No")
