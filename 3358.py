"""Pig"""
def main():
    """main"""
    n = int(input())
    w = list(map(int, input().split()))

    maxs = [max(w[2*i], w[2*i + 1]) for i in range(n)]

    if n == 1:
        print(maxs[0])
    else:
        print(" + ".join(map(str, maxs)) + " = " + str(sum(maxs)))

main()
