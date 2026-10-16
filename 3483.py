"""มาเป็นทีม"""
def main():
    """main"""
    n, m = map(int, input().split())

    if not (1 <= n <= 10 and 1 <= m <= 20):
        print("Data Incorrect")
    else:
        scores = [list(map(int, input().split())) for _ in range(n)]
        for i, team in enumerate(scores, 1):
            print(f"Team {i}: Average = {sum(team) / m:.2f}, Max = {max(team)}")
        print("Total Score of All Teams =", sum(map(sum, scores)))
main()
