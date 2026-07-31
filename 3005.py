'''rabbitgotomarket'''
def main():
    '''main'''
    carrot, cabbage, tomato = map(int ,input().split())
    paid = (carrot * 10) + (cabbage * 25) + (tomato * 3)
    print(paid)

main()
