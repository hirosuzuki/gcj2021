T = int(input())

def solve(no: int):
    vs = input().split()
    X = int(vs[0]) #CJ
    Y = int(vs[1]) #JC
    S = vs[2]
    INF = 100000000000000
    dp = [[0, 0] for _ in range(len(S))] # C,J
    
    c = S[0]
    if c == "?":
        dp[0] = [0, 0]
    elif c == "C":
        dp[0] = [0, INF]
    elif c == "J":
        dp[0] = [INF, 0]

    for i in range(1, len(S)):
        c = S[i]
        if c == "?":
            dp[i][0] = min(dp[i-1][0], dp[i-1][1] + Y)
            dp[i][1] = min(dp[i-1][0] + X, dp[i-1][1])
        elif c == "C":
            dp[i][0] = min(dp[i-1][0], dp[i-1][1] + Y)
            dp[i][1] = INF
        elif c == "J":
            dp[i][0] = INF
            dp[i][1] = min(dp[i-1][0] + X, dp[i-1][1])
    # print(dp)
    result = min(dp[-1])
    print(f"Case #{no}:",result)

for i in range(T):
    solve(i + 1)
