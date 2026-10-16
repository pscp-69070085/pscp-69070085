"""พูดจาภาษากระต่าย"""
def main():
    """main"""
    s = input().strip().upper()
    n = len(s)

    if all(c in "IT" for c in s):
        print("unknown", n)
    else:
        bad = -1
        for i, c in enumerate(s):
            if c not in "RABIT":
                bad = i
            elif c == "A":
                if not i or s[i - 1] not in "RA":
                    bad = i
            elif c == "R":
                if i + 1 >= n or s[i + 1] != "A":
                    bad = i + 1
            elif c == "B":
                if i + 1 >= n or s[i + 1] not in "IT":
                    bad = i + 1
            if bad != -1:
                break

        if bad != -1:
            print("no", bad)
        else:
            runs = s
            for ch in "RBIT":
                runs = runs.replace(ch, " ")
            print("yes", max(map(len, runs.split()), default=0))
main()
