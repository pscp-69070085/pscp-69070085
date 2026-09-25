"""Ticket"""
def main():
    """main"""
    age_day = input().split()
    age = int(age_day[0])

    if age_day[1] == "Wed":
        if age < 5:
            print(0)
        elif 5 <= age <= 18:
            print(50)
        else:
            print(75)
    else:
        if age < 5:
            print(0)
        elif 5 <= age <= 18:
            print(100)
        else:
            print(150)

main()
