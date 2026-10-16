"""[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"""
def main():
    """main"""
    n, p = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    for row in grid:
        bad_tiles = sum(1 for x in row if x > 0)
        print(*row, bad_tiles, sum(row))

    col_tiles = [sum(1 for r in range(n) if grid[r][c] > 0) for c in range(n)]
    col_points = [sum(grid[r][c] for r in range(n)) for c in range(n)]
    print(*col_tiles)
    print(*col_points)

    total_tiles = sum(col_tiles)
    total_points = sum(col_points)
    print(total_tiles, total_points, f"{total_points * p:.2f}")
main()
