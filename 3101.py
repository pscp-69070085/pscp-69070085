"""water"""
def main():
    """main"""
    temp = int(input())
    typee = input().lower()
    match typee:
        case "c":
            if temp <= 0:
                print("solid")
            elif temp >= 100:
                print("gas")
            else:
                print("liquid")
        case "f":
            if temp <= 32:
                print("solid")
            elif temp >= 212:
                print("gas")
            else:
                print("liquid")
main()
