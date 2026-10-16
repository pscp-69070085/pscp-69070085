'''A-E-I-O-U'''
def main():
    '''main'''
    sara = input().lower()
    if sara.count("a") > 0:
        print(f'a : {sara.count("a")}')
    if sara.count("e") > 0:
        print(f'e : {sara.count("e")}')
    if sara.count("i") > 0:
        print(f'i : {sara.count("i")}')
    if sara.count("o") > 0:
        print(f'o : {sara.count("o")}')
    if sara.count("u") > 0:
        print(f'u : {sara.count("u")}')

main()
