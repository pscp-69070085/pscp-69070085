"""โรงแรมกลางกรุง ไม่มีชั้น 13"""
def main():
    """main"""
    num = input()
    yo = [int(i) for i in num]
    room = ""
    for i in range(5):
        if yo[i] > 5 and i == 4:
            room += "14"
            break
        if yo[i] > 5:
            room += str(9 + i)
            break
    if not room:
        room += "13"

    if (num == num[::-1] and yo[0] + yo[4] > 5) or\
        (yo[4] and yo[0] // yo[4] > 5):
        room += "1"
    elif (num == num[::-1] and yo[1] * yo[3] > 5) or\
        (yo[1] - yo[4] > 5):
        room += "2"
    else:
        room += "0"

    total = sum(yo)

    chat = 1
    for i in yo:
        chat *= i

    if total > 25:
        room += "1"
    elif chat > 55:
        room += "2"
    else:
        room += "0"
    print(room)
main()
