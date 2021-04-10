T = int(input())

from typing import List, Tuple

def solve(no: int):
    M = int(input())
    PN = [[int(_) for _ in input().split()] for _ in range(M)]

    def solve1() -> int:
        tsn = sum(n for _, n in PN)
        if tsn > 100:
            return 0

        sn = sum(p*n for p, n in PN)
        #print("sn", sn)

        result = 0

        xs = [(1, 0)]
        for p, n in PN:
            ys: List[Tuple[int, int]] = []
            for s, ns in xs:
                for i in range(n + 1):
                    c, d = s * p**i, ns + p*i
                    if c <= sn:
                        ys.append((c, d))
                        if sn == c + d:
                            result = max(result, c)
            xs = ys
        #print("*", len(xs), xs)

        return result

    result = solve1()

    print(f"Case #{no}:",result)

for i in range(T):
    solve(i + 1)
