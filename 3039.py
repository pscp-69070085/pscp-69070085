"""loop find min 4"""
def main():
    """main"""
    n = int(input())
    if n <= 0:
        return

    lowest = int(input())

    for _ in range(n - 1):
        num = int(input())
        if num < lowest:
            lowest = num

    print(lowest)

main()
