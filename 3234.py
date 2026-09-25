"""ไฟคริสตมาส"""
def main():
    """main"""
    xmas = input().split()
    ream = xmas[0]
    num = int(xmas[1])
    lineupcolor = {"R": 0, "G": 1, "B": 2}
    color = ["Red","Green","Blue"]
    yo = lineupcolor[ream]
    last = []
    for _ in range(num):
        last.append(color[yo])
        yo = (yo + 1) % 3
    print(" ".join(last))
main()
