"""ตัวเลขโรมันแบบง่าย"""
def main():
    """main"""
    num = int(input())

    if num < 0:
        print("Error : Please input positive number")
    elif not num or num > 9:
        print("Error : Out of range")
    else:
        roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        print(roman_numerals[num - 1])

main()
