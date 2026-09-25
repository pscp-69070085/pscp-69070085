
"""main"""
def main():
    """หลัก"""
    size_type =  input().split()
    topping = input().split()
    size = size_type[0]
    total = 0
    match size:
        case "S":
            total += 60
        case "M":
            total += 80
        case "L":
            total += 100
    if size_type[1] == "T":
        total += 20
    match topping[0]:
        case "P":
            total += int(topping[1]) * 15
        case "E":
            total += int(topping[1]) * 10
    print(total)
main()
