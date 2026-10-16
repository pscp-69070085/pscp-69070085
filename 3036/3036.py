"""ปราสาท"""
import math as m
def main():
    """main"""
    room_n = int(input())

    if room_n == 1:
        print(0)
        return

    row = m.ceil(m.sqrt(room_n))

    fristrow = (row - 1) ** 2 + 1
    rows = room_n - fristrow + 1

    if rows % 2 :
        ans = 2 * (row - 1)
    else:
        ans = 2 * row - 3

    print(ans)

main()
