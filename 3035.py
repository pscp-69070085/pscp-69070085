'''ฟิลเตอร์ AR TikTok'''
def main():
    '''main'''
    r, x, y = map(int, input().split())
    dist = x**2 + y**2
    radius = r**2

    if dist < radius:
        print("IN")
    elif dist == radius:
        print("ON")
    else:
        print("OUT")

main()
