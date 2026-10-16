"""ลอดสะพาน"""
def main():
    """main"""
    length, n = map(int, input().split())
    diff = [0] * (length + 2)

    for _ in range(n):
        a, b = map(int, input().split())
        diff[a] += 1
        diff[b] -= 1

    best = 0
    current = 0
    for k in range(length + 1):
        current += diff[k]
        best = max(best, current)

    print(best)

main()
