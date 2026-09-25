"""ผลรวมของค่าที่มากกว่า"""
def main():
    """main"""
    n = int(input())
    maxn = []
    for _ in range(n):
        n1 = int(input())
        n2 = int(input())
        maxn.append(max(n1, n2))

    if n == 1:
        print(maxn[0])
    else:
        expression = ""
        for i in maxn:
            expression += str(i) + " + "
        expression = expression[:-3]
        total = sum(maxn)
        print(f"{expression} = {total}")
main()
