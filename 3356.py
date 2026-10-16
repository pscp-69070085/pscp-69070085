"""Bus Seat"""
def main():
    """main"""
    k = int(input())
    r = int(input())
    mine = int(input())

    for j in range(k):
        if j > 0 and not j % 2:
            print()
        row = []
        for c in range(r):
            seat = c * k + (k - j)
            row.append("XX" if seat == mine else f"{seat:02d}")
        print(" ".join(row))
main()
