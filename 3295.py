"""Electric_Using"""
def main():
    """main"""
    N = int(input())
    yo = N
    unit = 0

    if yo > 200:
        unit += (yo - 200) * 15
        yo = 200
    if yo > 100:
        unit += (yo - 100) * 12
        yo = 100
    if yo > 50:
        unit += (yo - 50) * 10
        yo = 50
    if yo > 10:
        unit += (yo - 10) * 7
        yo = 10
    if yo > 0:
        unit += yo * 5
    total = (unit * 1.07) + (N * 0.5)
    print(f"{total:.1f}")

main()
