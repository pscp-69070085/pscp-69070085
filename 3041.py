"""หารลงตัว"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())

    if num2 and not num1 % num2:
        print("yes")
    else:
        print("no")

main()
