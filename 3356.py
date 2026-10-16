"""Bus Seat"""
def main():
    """main"""
    k = int(input())
    r = int(input())
    target = int(input())

    for i in range(1, r + 1):
        col = []
    for j in range(k, 0, -1):
        seat = (i - 1) * k + j
        if seat == target:
            col.append("XX")
        else:
            col.append(f"{seat:02d}")
    print(" ".join(col))
    if i == r // 2:
        print()
main()
