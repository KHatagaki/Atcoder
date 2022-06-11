n,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
flag = True
dp = [False] * n
ep = [False] * n
dp[0] = True
ep[0] = True

for i in range(n-1):
    if dp[i] == True:
        if abs(a[i] - a[i+1]) <= k:
            dp[i+1] = True
        if abs(a[i] - b[i+1]) <= k:
            ep[i+1] = True
    if ep[i] == True:
        if abs(b[i] - a[i+1]) <= k:
            dp[i+1] = True
        if abs(b[i] - b[i+1]) <= k:
            ep[i+1] = True
if(ep[n-1] == True or dp[n-1] == True):
    print("Yes")
else:
    print("No")
