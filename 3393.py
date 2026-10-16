"""นักสำรวจถ้ำ (Cave Explorer)"""
def main():
    """main"""
    n = int(input())
    cave = list(map(int, input().split()))
    moves = input().strip()

    pos = cave.index(1)
    treasure = cave.index(2)
    cave[pos] = 0

    for move in moves:
        if move == "R" and pos < n - 1:
            pos += 1
        elif move == "L" and pos > 0:
            pos -= 1
        if pos == treasure:
            break

    cave[pos] = 1
    print(*cave)
main()
