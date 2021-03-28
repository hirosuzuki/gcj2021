T = int(input())

def solve(no: int):
    N = int(input())
    L = [int(_) for _ in input().split()]
    result = 0
    for i in range(N - 1):
        minv = 100000000000
        minvpos = 0
        for k in range(i, N):
            if minv > L[k]:
                minv = L[k]
                minvpos = k
        L = L[:i] + L[i:minvpos+1][::-1] + L[minvpos+1:]
        #print(i, minvpos, L)
        result += (minvpos - i + 1)
    print(f"Case #{no}:",result)

for i in range(T):
    solve(i + 1)
