N = input()
cnt=0
list = list(map(int,input().split()))
while True:
    even_list = [i/2 for i in list if i % 2 == 0]
    if len(list) != len(even_list):
        break
    list = even_list
    cnt += 1
print(cnt)