"""ค่าน้อยสุด"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if num1 <= num2 and num1 <= num3:
        ans = num1
    elif num2 <= num1 and num2 <= num3:
        ans = num2
    else:
        ans = num3

    print(ans)

main()
