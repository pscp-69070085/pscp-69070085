"""มากี่คน"""
def main():
    """main"""
    male = 0
    female = 0

    while True:
        n = int(input())
        if n < 0:
            break

        if n % 2:
            male += 1
        else:
            female += 1

    print(male, female, male + female)
main()
