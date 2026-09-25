"""พิมพ์สัญลักษณ์"""
def main():
    """main"""
    n = int(input())
    last = ""
    for i in range(1, n+1):
        if not i % 5:
            last += "X"
        else:
            last += "*"
    print(last)

main()
