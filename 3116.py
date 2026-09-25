"""นวัตกรรมงบประมาณโรงเรียน"""
import sys
def main():
    """main"""
    text = sys.stdin.read().rstrip('\r\n')
    if not text:
        return
    
    n = len(text)
    first_char_ascii = ord(text[0].upper())
    last_char_ascii = ord(text[-1].upper())

    step1 = []
    for pos in range(1, 11):
        v = pos - 1
        if pos % 2 == 0:
            val = first_char_ascii + v
        else:
            val = last_char_ascii - v
        step1.append(val)

    step2 = []
    for val in step1:
        rem = val % n
        if rem > 9:
            rem = rem % 10
        step2.append(rem)

    middle_digits = step2[2:8]
    pos_values = list(range(2, 8)) # values 2,3,4,5,6,7
    
    result_digits = []
    for digit, v in zip(middle_digits, pos_values):
        final_val = (digit + v) % 10
        result_digits.append(final_val)
    
    print(*(result_digits))

main()
