'''โปรแกรมรับรหัสประชาชน'''
def main():
    '''main'''
    idcard = int(input())
    yoyo = str(idcard)
    if len(yoyo) == 13:
        print("yes")
    else :
        print("no")

main()
