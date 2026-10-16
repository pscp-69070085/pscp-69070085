"""ติดตั้งหลอดไฟ"""
def main():
    """main"""
    n = int(input())
    heights = sorted(int(input()) for _ in range(n))

    total = 0
    prefix = 0
    for h in heights:
        prefix += h
        total += 2 * prefix

    print(total)
main()
