n = int(input())

s_x,s_y,t_x,t_y = map(int,input().split())

x = []
y = []
r = []

connect_list = []
start = 0
end = 0
for i in range(n):
    x_i,y_i,r_i = map(int,input().split())
    x.append(x_i)
    y.append(y_i)
    r.append(r_i)
    if (((s_x-x_i)**2 + (s_y-y_i)**2))**0.5 == r_i:
        start = i
    elif (((t_x-x_i)**2 + (t_y-y_i)**2))**0.5 == r_i:
        end = i

for i in range(n):
    mini_list = [i]
    for j in range(n):
        if i == j:
            continue
        distance = (x[i] - x[j])**2 + (y[i] - y[j])**2
        if (distance <= (r[i] + r[j])**2 and x[i] != x[j] and y[i] != y[j]):
            mini_list.append(j)
    connect_list.append(mini_list)
al_list = [start]

while True:
    if connect_list[start] == []:
        break
    if connect_list[start][0] == end:
        print("Yes")
        exit()
    if connect_list[start][0] in al_list:
        connect_list[start] = connect_list[start][1:]
    else:
        connect_list[start] += connect_list[connect_list[start][0]]
        al_list.append(connect_list[start][0])

print("No")
