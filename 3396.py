"""แซงรอบ"""
def main():
    """main"""
    n, k = map(int, input().split())
    times = [int(input()) for _ in range(n)]
    fastest = min(times)

    count = 0
    for t in times:
        if k * (t - fastest) < t:
            count += 1

    print(count)
main()
