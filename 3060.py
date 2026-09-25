"""การตรวจสอบสระ"""
def main():
    """main"""
    ch = input().strip()

    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("yes")
    else:
        print("no")

main()
