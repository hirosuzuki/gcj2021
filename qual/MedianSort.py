import sys

T, N, Q = [int(_) for _ in input().split()]

def rinput(x1: int, x2: int, x3: int) -> int:
    print(f"{x1} {x2} {x3}")
    sys.stdout.flush()
    return int(input())

def solve(no: int) -> int:
    result = rinput(1, 2, 3)
    xs = [[2, 1, 3], [1, 2, 3], [1, 3, 2]][result - 1]
    #print(xs)
    for n in range(4, N + 1):
        result = rinput(xs[0], xs[-1], n)
        if result == xs[0]:
            xs = [n] + xs
        elif result == xs[-1]:
            xs = xs + [n]
        else:
            l = 1
            r = len(xs) - 1
            while True:
                m = (l + r) // 2
                #print("#", xs, l, r, m)
                result = rinput(xs[m-1], xs[m], n)
                if result == n:
                    xs = xs[:m] + [n] + xs[m:]
                    break
                elif result == xs[m-1]:
                    r = m - 1
                elif result == xs[m]:
                    l = m + 1
    print(*xs)
    sys.stdout.flush()
    result = int(input())
    return result

for i in range(T):
    if solve(i + 1) != 1:
        break
