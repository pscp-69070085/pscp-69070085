'''สหกรณ์โรงเรียน'''
from decimal import Decimal, ROUND_HALF_UP
def main():
    is_member = input().strip()
    n = int(input().strip())
    total = sum(Decimal(input().strip()) for _ in range(n))

    if is_member == 'Y':
        total *= Decimal('0.95')
    elif is_member == 'N' and total >= 500:
        total *= Decimal('0.97')

    ans = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    print(f"{ans:.2f}")

main()
