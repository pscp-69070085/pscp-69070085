"""สลากกินแบ่ง"""
def main():
    """main"""
    a, b = input().split()
    x, y = input().split()

    if a == x and b == y:
        print (1000000)

    elif a != x and b == y:
        print (100000)

    elif a == x and b[2:5] == y[2:5]:
        print (2000)

    elif a == x and b[3:5] == y[3:5]:
        print (1000)

    elif a != x and b[2:5] == y[2:5]:
        print (200)

    elif a != x and b[3:5] == y[3:5]:
        print (100)

    elif a == x and b != y:
        print (20)

    else:
        print (0)
main()
