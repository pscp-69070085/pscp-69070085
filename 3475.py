"""Muddled Menu"""
def main():
    """main"""
    menu = []

    while True:
        line = input().strip()
        if line == "DONE":
            break
        if line == "CLOSED":
            menu.clear()
            break
        if line == "SOMETHING'S WRONG":
            menu.clear()
        elif line.startswith("Can't do: "):
            name = line[len("Can't do: "):]
            if name in menu:
                menu.remove(name)
        else:
            name, pos = line.rsplit(" #", 1)
            if pos == "N":
                menu.append(name)
            else:
                menu.insert(int(pos) - 1, name)

    print("Full Course:", menu, "Reversed:", menu[::-1])
main()
