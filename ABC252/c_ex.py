n = int(input())
 
s = []
for i in range(n):
    s.append(input())
 
#print(s)
 
dp = [[-1 for _ in range(10)]for __ in range(len(s))]
 
for i in range(10):
    dp[0][int(s[0][i])] = i
idx = 0
cnt = -1
for i in range(1,n):
    for j in range(10):
        dp[i][int(s[i][j])] = max(dp[i-1][int(s[i][j])], j)
        for k in range(n):
            if(s[k][j] == s[i][j]):
                cnt += 1
        if(cnt >= 1):
            dp[i][int(s[i][j])] += 10
        cnt = -1
 
print(min(dp[n-1]))