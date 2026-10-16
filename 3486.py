"""ตำบลกระสุนตก"""
def main():
    """main"""
    n = int(input())
    shots = [list(map(int, input().split())) for _ in range(n)]
    x1, y1, d1 = shots[0]
    found = False

    for tx in range(x1 - d1, x1 + d1 + 1):
        for ty in range(y1 - d1, y1 + d1 + 1):
            if found:
                break
            ok = True
            for x, y, d in shots:
                if (tx - x) ** 2 + (ty - y) ** 2 != d * d:
                    ok = False
            if ok:
                print(tx, ty)
                found = True
main()
