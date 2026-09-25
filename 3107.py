"""bonus"""
def age_percent(a, s, j):
    """check age percent"""
    if a <= 5:
        match j:
            case "M":
                return 0.06*s
            case "B":
                return 0.05*s
            case "G":
                return 0.04*s
    elif 5 < a <= 10:
        match j:
            case "M":
                return 0.08*s
            case "B":
                return 0.06*s
            case "G":
                return 0.05*s
    elif a > 10:
        match j:
            case "M":
                return 0.1*s
            case "B":
                return 0.07*s
            case "G":
                return 0.06*s
    return 0

def main():
    """main"""
    info = input().split()
    match info[0]:
        case "M":
            print(round((age_percent(int(info[1]), int(info[2]), info[0])) + 1500))
        case "B":
            print(round((age_percent(int(info[1]), int(info[2]), info[0])) + 1000))
        case "G":
            print(round((age_percent(int(info[1]), int(info[2]), info[0])) + 500))

main()
