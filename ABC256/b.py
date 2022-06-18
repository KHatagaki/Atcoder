n = int(input())

a = list(map(int,input().split()))

mass_to = [0] * 4

p = 0

for i in range(len(a)):
    mass_to[0] = 1
    mass_from = [0] * 4
    for j in range(4):
        if(mass_to[j] == 1):
            if(j + a[i] >= 4):
                p += 1
            else:
                mass_from[j + a[i]] = 1
    mass_to = mass_from

print(p)
