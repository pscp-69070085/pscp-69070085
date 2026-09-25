'''over'''
def main():
    '''main'''
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())

    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    rad = (r1 + r2) ** 2

    if dist <= rad:
        print("overlapping")
    else:
        print("no overlapping")

main()
