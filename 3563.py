"""PSCP-P02 ผลคูณเลขโดดที่ไม่เป็นศูนย์"""
def main():
    """main"""
    n = input()
    result = 1
    zero = False

    for char in n:
        digit = int(char)
        if digit:
            result *= digit
            zero = True
    if zero:
        print(result)
    else:
        print(0)

main()
