"""ขายรถยนต์"""
def main():
    """main"""
    n = int(input())
    v = []
    for _ in range(n):
        _ , s = input().split()
        v.append(int(s))

    best = 0
    cnt = 0
    for i in range(n - 1, -1, -1):
        if v[i] < best:
            cnt += 1
        else:
            best = v[i]

    print(cnt)
main()
