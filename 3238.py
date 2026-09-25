"""Elon Musk (X-shape)"""
def main():
    """main"""
    n ,k = input().split()
    n = int(n)
    mid = n // 2
    for i in range(n):
        row = []
        for j in range(n):
            if i == j or i + j == n - 1:
                if k == "#":
                    row.append("#")
                else:
                    yo = abs(i-mid)
                    chat = ord(k) + yo
                    row.append(chr(chat))
            else:
                row.append("-")
        print("".join(row))

main()
