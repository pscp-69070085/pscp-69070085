'''season'''
def main():
    '''check '''
    month = int(input())
    day = int(input())
    if month == 3 and day >= 21:
        print("spring")
    elif month == 6 and day >= 21:
        print("summer")
    elif month == 9 and day >= 21:
        print("fall")
    elif month == 12 and day >= 21:
        print("winter")
    elif month <= 3:
        print("winter")
    elif month <= 6:
        print("spring")
    elif month <= 9:
        print("summer")
    else:
        print("fall")
        
main()
