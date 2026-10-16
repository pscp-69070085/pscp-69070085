"""Resistor"""
def main():
    """main"""
    digits = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "purple": 7, "grey": 8, "white": 9,
    }
    multipliers = {
        "black": 1, "brown": 10, "red": 100, "orange": 1000,
        "yellow": 10000, "green": 100000, "blue": 1000000,
        "purple": 10000000, "gold": 0.1, "silver": 0.01,
    }
    tolerances = {
        "brown": 1, "red": 2, "green": 0.5, "blue": 0.25,
        "purple": 0.1, "grey": 0.05, "gold": 5, "silver": 10,
    }

    c1, c2, c3, c4 = (input().strip().lower() for _ in range(4))
    d1 = digits.get(c1)
    d2 = digits.get(c2)
    mult = multipliers.get(c3)
    tol = tolerances.get(c4)

    if None in (d1, d2, mult, tol):
        print("Error")
        return

    value = (d1 * 10 + d2) * mult
    print(f"{value * (1 - tol / 100):.4f}")
    print(f"{value * (1 + tol / 100):.4f}")
main()
