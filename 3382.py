"""Day08-0_02-Backward"""
def main():
    """main"""
    lines = []
    while True:
        s = input()
        if s == "NULL":
            break
        lines.append(s)

    for s in reversed(lines):
        print(s)
main()  
