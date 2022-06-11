n = int(input())
c = []
s = []

for i in range(n):
    for j in range(i+1):
        if(j == 0 or j == i):
            print("1",end=" ")
            s.append(1)
        else:
            print(c[j-1]+c[j],end=" ")
            s.append(c[j-1]+c[j])
    print("")
    c = s
    s = []