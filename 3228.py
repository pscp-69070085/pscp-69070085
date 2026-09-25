"""การนับสระ"""
def main():
    """main"""
    word = input()
    sara = "aeiou"
    total = 0
    for char in word:
        if char in sara:
            total += 1
    print(total)
main()
