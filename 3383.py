"""Difference"""
def main():
    """main"""
    n = int(input())
    m = int(input())
    a = set(int(input()) for _ in range(n))
    b = set(int(input()) for _ in range(m))
    result = sorted(a - b)
    print(*result)
main()
