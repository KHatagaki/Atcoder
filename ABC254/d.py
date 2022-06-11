n = int(input())

sum = 0 

for i in range(1,n+1):
    for j in range(i,n+1):
        if ((i*j) ** .5).is_integer():
            sum += 1
print(sum*2 - n)
