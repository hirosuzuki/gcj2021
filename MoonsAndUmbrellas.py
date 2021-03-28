T = int(input())

def solve(no: int):
    vs = input().split()
    X = int(vs[0])
    Y = int(vs[1])
    S = vs[2]
    result = 0
    s = S.replace("?", "")
    for i in range(len(s) - 1):
        ss = s[i:i+2]
        if ss == "CJ":
            result += X
        elif ss == "JC":
            result += Y
    print(f"Case #{no}:",result)

for i in range(T):
    solve(i + 1)
