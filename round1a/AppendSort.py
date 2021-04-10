T = int(input())

def solve(no: int):
    N = int(input())
    X = [_ for _ in input().split()]
    result = 0
    a = "0"
    for x in X:
        if int(x) > int(a):
            pass
        elif len(x) == len(a):
            x = x + "0"
            result += 1
        else:
            a1, a2 = a[:len(x)], a[len(x):]
            if x > a1:
                x = x + "0" * len(a2)
                result += len(a2)
            elif x < a1:
                x = x + "0" * len(a2) + "0"
                result += len(a2) + 1
            else:
                if a2 == "9" * len(a2):
                    x = x + "0" * len(a2) + "0"
                    result += len(a2) + 1
                else:
                    x = x + ("0" * 100 + str(int(a2) + 1))[-len(a2):]
                    result += len(a2)
        #print(a, x)
        a = x
    print(f"Case #{no}:",result)

for i in range(T):
    solve(i + 1)
