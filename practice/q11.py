n = int(input())
t_list = []
x_list = []
y_list = []
now_place = [0,0]
now_time = 0
flag = True 

for i in range(0,n):
    t,x,y = map(int,input().split())
    t_list.append(t)
    x_list.append(x)
    y_list.append(y)

for t,x,y in zip(t_list,x_list,y_list):
    tgt_time = t
    tgt_place = [x,y]
    diff_x = tgt_place[0] - now_place[0]
    diff_y = tgt_place[1] - now_place[1]
    time_margin = tgt_time-now_time-abs(diff_x)-abs(diff_y)
    if time_margin < 0:
        flag = False
        break
    elif  time_margin % 2 == 0:
        now_time = tgt_time
        now_place = [x,y]
    else:
        flag = False
        break

if (flag == True):
    print("Yes")
else:
    print("No")