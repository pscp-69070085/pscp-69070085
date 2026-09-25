""" ไพ่ 44 ใบ"""
def main():
    """main"""
    card = input().upper()
    nc = {"A": "ace", "J": "jack", "Q": "queen", "K": "king"}
    suits = {"D": "diamonds", "H": "hearts", "S": "spades", "C": "clubs"}
    r = nc.get(card[:-1], card[:-1])
    s = suits[card[-1]]

    print(f"{r} of {s}")
main()
