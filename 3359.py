"""กองชาม"""
def main():
    """main"""
    n = int(input())
    count = {}
    for _ in range(n):
        x = input().strip()
        count[x] = count.get(x, 0) + 1

    print(max(count.values()))
main()
