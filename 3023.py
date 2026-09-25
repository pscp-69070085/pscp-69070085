'''Calculator'''
def main():
    '''main'''
    num = int(input())
    if num == 1:
        print(1)
    else:
        total = 0
        for i in range(1,num + 1):
            total += len(str(i)) + 1
        print(total)

main()
