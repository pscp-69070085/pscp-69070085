"""วิเคราะห์ยอดขายร้านกาแฟ"""
def main():
    """main"""
    n = int(input())
    coffee = []
    for _ in range(n):
        coffee.append(int(input()))

    print(sum(coffee))
    print(max(coffee))
    print(min(coffee))
    print(f"{sum(coffee)/n:.1f}")

main()
