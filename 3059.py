"""ผลการสอบ"""
def main():
    """main"""
    hw = float(input())
    mid = float(input())
    final = float(input())

    if hw >= 5 and mid >= 20 and final >= 25:
        print("pass")
    else:
        print("fail")

main()
