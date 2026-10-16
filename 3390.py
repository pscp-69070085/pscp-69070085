"""Array 2D ตรวจสอบ"""
def main():
    """main"""
    grid = [list(map(int, input().split())) for _ in range(5)]
    row = -1
    col = -1
    for i in range(5):
        if sum(grid[i]) % 2 == 1:
            row = i
    for j in range(5):
        if sum(grid[i][j] for i in range(5)) % 2 == 1:
            col = j
    print(row, col)
main()
