"""พอด"""
def main():
    """main"""
    n, k = map(int, input().split())
    queues = [0] * k
    active = 0
    served = 0

    for _ in range(n):
        q = int(input()) - 1
        if not queues[q]:
            active += 1
        queues[q] += 1

        if active == k:
            served += k
            for j in range(k):
                queues[j] -= 1
                if not queues[j]:
                    active -= 1

    print(n - served)

main()
