"""เกมทายลูกเต๋า"""
def main():
    """main"""
    g = int(input())
    r = int(input())
    dice = [1,2,3,4,5,6]
    if g in dice and r in dice:
        if g == r:
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Invalid")
main()
