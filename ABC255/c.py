x,a,d,n = map(int,input().split())
flag = 0
cnt = 1
left = 0
right = n - 1
mid = right - left
if d > 0:
    while True:
        print(mid)
        if (x > a + d * mid and x - d < a + d * mid):
            flag = -1
            break
        elif(x < a + d * mid and x + d > a + d * mid):
            flag = 1
            break
        elif (x > a + d * mid):
            left = mid
            mid += right - left
        elif (x < a + d * mid):
            right = mid
            mid -= right - left
        else:
            break
elif d < 0:
    while True:
        print(mid)
        if (x < a + d * mid and x - d < a + d * mid):
            flag = -1
            break
        elif(x > a + d * mid and x + d > a + d * mid):
            flag = 1
            break
        elif (x < a + d * mid):
            left = mid
            mid += right - left
        elif (x > a + d * mid):
            right = mid
            mid -= right - left
        else:
            break
else:
    print(abs(x-a))
    exit()

if(flag == -1):
    if(abs(x - a - d * mid) > abs(x - d - a - d * mid)):
        print(abs(x - d - a - d * mid))
    else:
        print(abs(x - a - d * mid))
elif(flag == 1):
    if(abs(x - a - d * mid) > abs(x + d - a - d * mid)):
        print(abs(x + d - a - d * mid))
    else:
        print(abs(x - a - d * mid))
else:
    print("0")