"""Tuple's Sad life"""
def main():
    """main"""
    t = tuple(input().split())
    x = input().strip()
    n = t.count(x)
    if n > 0:
        idx = t.index(x)
        for _ in range(n):
            print(*([idx] * n))
main()
