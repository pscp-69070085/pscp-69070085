"""coke"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    caps = 0
    cost = 0

    for _ in range(d):
        if caps >= b > 0:
            caps -= b
            cost += c
        else:
            cost += a
        caps += 1

    print(cost)

main()
