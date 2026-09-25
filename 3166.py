"""ผ่านหรือไม่ ค่าเฉลี่ยรายวิชา"""
def main():
    """main"""
    n = int(input())
    total = 0
    yochat = True
    for _ in range(n):
        score = int(input())
        total += score
        avg = total / n
        if score < 50 :
            yochat = False
    print(f"{avg:.1f}")
    if yochat and avg >= 60:
        print("PASS")
    else:
        print("FAIL")

main()
