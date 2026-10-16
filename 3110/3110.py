'''war'''
def main():
    '''main'''
    start, stop = input().upper().split()
    weight = float(input())
    if start == "BKK" and stop == "CNX":
        print(f"{weight * 30 + 10:.2f}")
    elif start == "CNX" and stop == "UBP":
        print(f"{weight * 40 + 15:.2f}")
    elif start == "UBP" and stop == "BKK":
        print(f"{weight * 40 + 20:.2f}")
    elif start == "BKK" and stop == "PKT":
        print(f"{weight * 50 + 25:.2f}")
    elif start == "PKT" and stop == "CNX":
        print(f"{weight * 60 + 30:.2f}")
    elif start == "UBP" and stop == "PKT":
        print(f"{weight * 70 + 40:.2f}")
    else:
        print("Error")
main()
