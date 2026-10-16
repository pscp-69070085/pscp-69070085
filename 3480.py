"""นก"""
def main():
    """main"""
    n = int(input())
    heights = list(map(int, input().split()))

    count = 0
    for i in range(n):
        left_ok = not i or heights[i] > heights[i - 1]
        right_ok = i == n - 1 or heights[i] > heights[i + 1]
        if left_ok and right_ok:
            count += 1

    print(count)
main()
