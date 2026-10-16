"""เข้าแถว"""
def main():
    """main"""
    n, _ = map(int, input().split())
    heights = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    prefix_max = [0] * n
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], heights[i - 1])

    for a in queries:
        i = a - 1
        if not i:
            print(0)
        else:
            print(max(0, prefix_max[i] + 1 - heights[i]))
main()
