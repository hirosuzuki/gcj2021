from math import sqrt

T = int(input())
P = int(input())

def solve(no: int):
    scores = [[(c == "1") for c in input()] for _ in range(100)]

    xs = [sum(scores[i][k] for i in range(100)) for k in range(1000)]
    # print(xs)

    ps = sorted(list(range(1000)), key=lambda x:xs[x])
    # print(ps)

    # for k in range(1000):
    #     print(ps[k], xs[ps[k]])

    result = 0
    minv = 100000000000000000
    for i in range(100):
        score = scores[i]
        cs = sum(score[ps[k]] * (k - 500) for k in range(1000))
        v = cs
        if minv > v:
            minv = v
            result = i + 1
        # print(i, cs, v)

    print(f"Case #{no}:",result)

for i in range(T):
    solve(i + 1)
