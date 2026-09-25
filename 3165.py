"""เดินเล่นในงานเทศกาล"""
def main():
    """main"""
    nsew = input()
    x = 0
    y = 0
    for char in nsew:
        if char == "N":
            y += 1
        elif char == "S":
            y -= 1
        elif char == "E":
            x += 1
        elif char == "W":
            x -= 1

    dis = abs(x) + abs(y)
    print(x ,y ,dis)

main()
