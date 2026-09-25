'''temperture'''
def main():
    '''main'''
    temp = float(input())
    before = input()
    after = input()
    celsius = 0
    last = 0

    if before == "C":
        celsius = temp
    elif before == "F":
        celsius = (temp - 32) * 5 / 9
    elif before == "K":
        celsius = temp - 273.15
    elif before == "R":
        celsius = (temp * 5 / 9) - 273.15

    if after == "C":
        last = celsius
    elif after == "F":
        last = celsius * 9 / 5 + 32
    elif after == "K":
        last = celsius + 273.15
    elif after == "R":
        last = (celsius + 273.15) * 9 / 5

    print(f"{last:.2f}")

main()
