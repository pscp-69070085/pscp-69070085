"""ค่าตั๋ว"""
def main():
    """main"""
    age = int(input())
    status = input().lower()

    if age < 18 or status == 's':
        print(20)
    else:
        print(50)

main()
