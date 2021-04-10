T = int(input())

from typing import List, Tuple
from math import gcd

def solve(no: int):
    N, Q = [int(x) for x in input().split()]
    AS = [input().split() for _ in range(N)]
    A = [int(x[0].replace("T", "1").replace("F", "0"), 2) for x in AS]
    S = [int(x[1]) for x in AS]

    def calc(x: int, y: int, n: int) -> int:
        result = 0
        z = x ^ y
        for i in range(n):
            if z & 1 == 0:
                result += 1
            z >>= 1
        #print(x, y, n, result)
        return result

    def solve1():
        if Q > 10:
            return 0

        ns = []
        for n in range(2**Q):
            if all(calc(n, A[j], Q) == S[j] for j in range(N)):
                ns.append(n)

        #print("*", ns)

        result = (0, 0)


        rs = [""] * Q
        rr = 0
        rz = 0
        rw = len(ns)
        for i in range(Q):
            p = sum([((n & (1<<i)) > 0) for n in ns])
            c = "F"
            if p > len(ns) // 2:
                c = "T"
            else:
                p = len(ns) - p
            rz += p
            
            rs[Q - i - 1] = c
            #print(i, p, rs, rz)

        ry = "".join(rs)
        #rz = result[0]
        #rw = len(ns)
        g = gcd(rz, rw)
        rz //= g
        rw //= g
        return ry, rz, rw

    result = solve1()

    print(f"Case #{no}: {result[0]} {result[1]}/{result[2]}")

for i in range(T):
    solve(i + 1)
