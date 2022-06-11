q = int(input())
max = 0
min = 10 ** 9
s = []
for i in range(q): 
    q_in = list(map(int,input().split()))
    if(len(q_in) == 1):
        print(max-min)
    elif(len(q_in) == 2):
        if(max < q_in[1]):
            max = q_in[1]
        if(min > q_in[1]):
            min = q_in[1]
        if q_in[1] not in s:
            s.append([q_in[1],1])
        else:
            for j in range(len(s)):
                if(s[j][0] == q_in[1]):
                    s[j][1] = str(int(s[j][1]) + 1)
    else:
        for j in range(len(s)):
            if(s[j][0] == q_in[1] and int(s[j][1]) > 0):
                if(max < q_in[1]):
                    max = q_in[1]
                if(min > q_in[1]):
                    min = q_in[1]
                s[j][1] = str(int(s[j][1]) - min(q_in[2],int(s[j][1])))
                if(int(s[j][1]) < 0):
                    s[j][1] == "0"

