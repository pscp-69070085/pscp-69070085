'''Quadrant'''
def main():
    '''main'''
    X = int(input())
    Y = int(input())
    if not X and not Y :
        print("O")
    elif not Y :
        print("X")
    elif not X :
        print("Y")
    elif X >= 1 and Y >= 1 :
        print("Q1")
    elif X <= -1 and Y >= 1 :
        print("Q2")
    elif X <= -1 and Y <= -1 :
        print("Q3")
    elif X >= 1 and Y <= -1 :
        print("Q4")

main()
