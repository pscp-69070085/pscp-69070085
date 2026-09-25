"""กบน้อยกระโดด"""
def main():
    """main"""
    x ,y = map(int ,input().split())
    dis = 0
    jump = 0
    while x > 0 and dis < y:
        dis += x
        jump += 1
        x -= 2
    if dis >= y:
        print(jump)
    else:
        print(-1)

main()
