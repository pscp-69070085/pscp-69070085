"""ชานมไข่มุก"""
def main():
    """main"""
    boba_type, boba_g = input().split()
    tea_type, sweet, tea_cc = input().split()

    boba_cal = {'H': 5, 'O': 3, 'J': 2}
    tea_cal = {
        'R': [12, 18, 25],
        'T': [15, 20, 30],
        'M': [10, 15, 20]
    }

    total = int(boba_g) * boba_cal[boba_type] + int(tea_cc) * tea_cal[tea_type][int(sweet) - 1]
    print(total)

main()
