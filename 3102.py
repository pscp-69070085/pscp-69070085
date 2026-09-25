"""Tax Car"""
def find_ccc(stage, cc):
    """find cc"""
    match stage:
        case 1:
            if cc <= 1500:
                print(1250)
            elif 2000 >= cc > 1500:
                print(1400)
            elif cc > 2000:
                print(2000)
        case 2:
            if cc <= 1500:
                print(1100)
            elif 2000 >= cc > 1500:
                print(1300)
            elif cc > 2000:
                print(1700)
        case 3:
            if cc <= 1500:
                print(1000)
            elif 2000 >= cc > 1500:
                print(1200)
            elif cc > 2000:
                print(1500)

def main():
    """main"""
    year = int(input())
    cc = int(input())
    if year <= 1990:
        find_ccc(1, cc)
    elif 1991 <= year <= 1999:
        find_ccc(2, cc)
    else:
        find_ccc(3, cc)

main()
