"""[LEARNING LOGS] Pad Thai"""
def main():
    """main"""
    recipe = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts",
        "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts",
    }
    good_tastes = {"Sweet", "Sour", "Salty"}

    ingredients = set()
    while True:
        line = input().strip()
        if line == "Cook":
            break
        ingredients.add(line)

    tastes = set()
    while True:
        line = input().strip()
        if line == "End":
            break
        tastes.add(line)

    if not ingredients <= recipe:
        print("This is not Pad Thai!!!")
    elif ingredients != recipe:
        print("This is bad!")
    elif tastes != good_tastes:
        print("Not Bad...")
    else:
        print("Delicious!")
main()
