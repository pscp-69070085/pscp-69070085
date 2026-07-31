'''season'''
def main():
    '''check '''
    month = int(input())
    day = int(input())
    if month <= 3 and day < 21 :
        print("winter")
    elif 3 <= month <= 6 and day <= 21 :
        print("spring")
    elif 6 <= month <= 9 and day <= 21 :
        print("summer")
    elif 9 <= month <= 12 and day <= 21 :
        print("fall")

main()
