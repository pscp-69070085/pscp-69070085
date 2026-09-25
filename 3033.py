'''gifting'''
def main():
    '''main'''
    r, h, d = map(float, input().split())
    width = h+2*r
    length = 2*3.14*r + d
    print(f"{width:.2f} {length:.2f}")
main()
