a = input()

list = ["0","1","2","3","4","5","6","7","8","9"]

for i in list:
    if i in a:
        continue
    else:
        print(i)
        break
