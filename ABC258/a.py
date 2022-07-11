k = int(input())

time = k // 60
minute = k % 60
time += 21
if(minute < 10):
    minute = "0" + str(minute)
print(str(time) + ":" + str(minute))

