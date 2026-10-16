"""ไข้หวัดกระต่ายสายพันธุ์ใหม่"""
def main():
    """main"""
    yo, chat = map(int, input().split())
    cr, cc = map(int, input().split())
    n = int(input())

    grid = [[0] * chat for _ in range(yo)]

    for _ in range(n):
        r, c = map(int, input().split())
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                i, j = r + dr, c + dc
                if 0 <= i < yo and 0 <= j < chat:
                    d = max(abs(dr), abs(dc))
                    if not d:
                        v = 100
                    elif d == 1:
                        v = 60
                    else:
                        v = 20
                    if v > grid[i][j]:
                        grid[i][j] = v

    safe = sum(row.count(0) for row in grid)

    print(safe)
    print(str(grid[cr][cc]) + "%")
main()
