"""บุพเพสันนิวาส"""
def main():
    """main"""
    a = input().strip()
    b = input().strip()

    if len(a) < len(b):
        a += a[0] * (len(b) - len(a))
    else:
        b += b[0] * (len(a) - len(b))

    s = ""
    for x, y in zip(a, b):
        if x.lower() in "love" or y.lower() in "love":
            s += "w"
        else:
            s += "$"

    cnt = s.count("w")
    run = max(len(t) for t in s.split("$"))

    if cnt % 2 == 1:
        s += str(run)
    elif run < 2:
        s += "#"

    print(s)
main()
