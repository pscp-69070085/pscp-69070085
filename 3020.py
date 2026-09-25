'''coke'''
def main():
    '''main'''
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not b:
        coke = a * d
        print(coke)
    else:
        coke = ((d // b) * c) + ((d - (d // b)) * a)
        print(coke)

main()
