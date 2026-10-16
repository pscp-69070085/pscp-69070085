"""PickThemAgain"""
def main():
    """main"""
    num = list(map(int, input().split()))

    filtered = [x for x in num if not x % 3 or not x % 5]

    if not filtered:
        print("Nope")
    else:
        for n in reversed(filtered):
            print(n)

main()
