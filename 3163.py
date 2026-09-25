"""สินค้าส่งออก"""
def main():
    """main"""
    yo = []
    even = 0
    odd = 0
    for _ in range(int(input())):
        num = int(input())
        yo.append(num)

        if not num % 2:
            even += 1
        else:
            odd += 1
    print(f"SUM {sum(yo)}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")

main()
