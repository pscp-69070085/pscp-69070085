"""แลกเปลี่ยนเงิน"""
def main():
    """main"""
    money = int(input())

    coin10 = money // 10
    money %= 10

    coin5 = money // 5
    money %= 5

    coin2 = money // 2
    money %= 2

    coin1 = money

    print(f"10 = {coin10}")
    print(f"5 = {coin5}")
    print(f"2 = {coin2}")
    print(f"1 = {coin1}")

main()
