'''แม่สี (Primary Color) มี 3 สี คือ สีแดง (Red) สีเหลือง (Yellow) และสีน้ำเงิน (Blue)'''
def main():
    '''main'''
    color = input()
    color1 = input()
    if color == "Red" and color1 == "Red":
        print("Red")
    elif color == "Yellow" and color1 == "Yellow":
        print("Yellow")
    elif color == "Blue" and color1 == "Blue":
        print("Blue")
    elif color == "Red" and color1 == "Blue":
        print("Violet")
    elif color == "Red" and color1 == "Yellow":
        print("Orange")
    elif color == "Yellow" and color1 == "Blue":
        print("Green")
    elif color == "Blue" and color1 == "Red":
        print("Violet")
    elif color == "Yellow" and color1 == "Red":
        print("Orange")
    elif color == "Blue" and color1 == "Yellow":
        print("Green")
    else:
        print("Error")

main()
