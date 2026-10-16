"""3nPlus1"""
def main(n):
    """main"""
    memo = {1: 1}

    while True:
        n = int(input())
        if n == 0:
            break

        path = []
        curr = n

        while curr not in memo:
            path.append(curr)
            curr = curr // 2 if curr % 2 == 0 else 3 * curr + 1

        ans = memo[curr]
        for num in reversed(path):
            ans += 1
            memo[num] = ans

        print(memo[n])
main()
