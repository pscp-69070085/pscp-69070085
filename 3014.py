"""milk"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    nummilk = d // a
    milks = nummilk
    caps = nummilk

    if b > 0:
        for _ in range(nummilk + 1):
            if caps < b:
                break
            exchang = caps // b
            newmilk = exchang * c
            milks += newmilk
            caps = (caps % b) + newmilk

    print(milks)

main()
