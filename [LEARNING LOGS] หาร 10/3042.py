"""หาร 10"""
def main():
    """main"""
    n = int(input())
    start = n - (n % 10)

    print(*range(start, -1, -10))

main()
