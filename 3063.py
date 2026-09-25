"""รหัสเซฟ"""
def main():
    """main"""
    char_input = input().strip()
    num_input = int(input())

    is_char_correct = char_input == 'H'
    is_num_correct = num_input == 4567

    if is_char_correct and is_num_correct:
        print("safe unlocked")
    elif is_char_correct and not is_num_correct:
        print("safe locked - change digit")
    elif not is_char_correct and is_num_correct:
        print("safe locked - change char")
    else:
        print("safe locked")

main()
