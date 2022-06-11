from collections import deque
q = int(input())

query = []

for i in range(q):
    query.append(input())

inside = deque()

for que in query:
    sum = 0
    if que.split()[0] == "1":
        list = [que.split()[1]] * int(que.split()[2])
        inside.extend(list)
    else:
        for i in range(int(que.split()[1])):
            sum += int(inside.popleft())
        print(sum)