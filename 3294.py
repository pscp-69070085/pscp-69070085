"""Teaching schedule"""
def main():
    """main"""
    num = int(input())
    time = int(input())
    totalmin = num * time
    hours = totalmin // 60
    minn = totalmin % 60
    if not totalmin:
        print("No teaching")
    else:
        if totalmin < 60:
            print(f"{minn} minute")
        elif not minn:
            print(f"{hours} hours")
        else:
            print(f"{hours} hours {minn} minute")

main()
