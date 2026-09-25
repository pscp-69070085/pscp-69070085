"""Conan"""
def main():
    """main"""
    letter = input()
    n = int(input())
    result = []
    for char in letter:
        shifted = chr((ord(char) - ord("a") + n) % 26 + ord("a"))
        result.append(shifted)
    print("".join(result))

main()
