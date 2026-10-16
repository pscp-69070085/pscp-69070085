"""FourDirections"""
def main():
    """main"""
    s = input().strip()
    if not s:
        return

    arrows = {
    "U": ["  *  ", " *** ", "* * *", "  *  ", "  *  "],
    "D": ["  *  ", "  *  ", "* * *", " *** ", "  *  "],
    "L": ["  *  ", " *   ", "*****", " *   ", "  *  "],
    "R": ["  *  ", "   * ", "*****", "   * ", "  *  "],
    }

    for row in range(5):
        part = []
        for char in s:
            if char in arrows:
                part.append(arrows[char][row])
        print(" ".join(part))
main()
