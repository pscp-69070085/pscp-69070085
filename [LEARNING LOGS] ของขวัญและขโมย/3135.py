"""ของขวัญและขโมย"""
def main():
    """main"""
    N, K, T = map(int, input().split())
    yo = 0
    chat = 1

    while True:
        if chat == T:
            yo += 1
            break
        if chat == 1 and yo:
            break
        chat = (chat + K) % N
        yo += 1

    print(yo)
main()
