"""countsara"""
def main():
    """main"""
    list_letter = []
    count = 0
    sara = ["A", "E", "I", "O", "U"]

    for _ in range(int(input())):
        list_letter.append(input())

    for _, letter in enumerate(list_letter):
        for l in sara:
            if l == letter:
                count += 1
    print(count)

main()
