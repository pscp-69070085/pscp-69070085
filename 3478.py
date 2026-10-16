"""Easy Histogram"""
def main():
    """main"""
    text = input()

    for letter in "abcdefghijklmnopqrstuvwxyz":
        for ch in (letter, letter.upper()):
            count = text.count(ch)
            if count:
                print(f"{ch} = {count}")
main()
