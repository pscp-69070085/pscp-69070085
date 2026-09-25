"""เกมสะสมแต้ม"""
def main():
    """main"""
    n = 0
    for _ in range(int(input())):
        com = input()
        if com == "+":
            n += 10
        elif com == "-":
            n -= 5
    print(n)
main()
