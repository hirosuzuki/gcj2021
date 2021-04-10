from typing import List

T = int(input())

def calc(xs: List[int]):
    result = 0
    N = len(xs)
    for i in range(N - 1):
        minv = 100000000000
        minvpos = 0
        for k in range(i, N):
            if minv > xs[k]:
                minv = xs[k]
                minvpos = k
        xs = xs[:i] + xs[i:minvpos+1][::-1] + xs[minvpos+1:]
        result += (minvpos - i + 1)
    return result


def solve1(N: int, C: int):
    if C < N - 1:
        return "IMPOSSIBLE"
    xs = [1] * (N - 1)
    left = C - (N - 1)
    for i in range(N - 1):
        m = min(N - i - 1, left)
        xs[i] += m
        left -= m
    if left > 0:
        return "IMPOSSIBLE"
    vs = [N]
    for i in range(N - 1):
        v = N - 1 - i
        j = xs[N - 1 - i - 1]
        vs = vs[:j - 1][::-1] + [v] + vs[j - 1:]
    #print("#", calc(vs))
    return " ".join(map(str, vs))

def solve(no: int):
    N, C = [int(_) for _ in input().split()]
    print(f"Case #{no}:", solve1(N, C))

for i in range(T):
    solve(i + 1)
