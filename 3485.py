"""รหัสต้องไม่ซ้ำกัน"""
from collections import Counter
def main():
    """main"""
    _ = int(input())
    codes = list(map(int, input().split()))

    count = Counter(codes)
    print(*sorted(c for c in count if count[c] == 1))
main()
