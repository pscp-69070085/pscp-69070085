"""BrickBridge"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    goal = int(input())

    max_big_needed = goal // 5
    big_used = min(b, max_big_needed)

    remaining_length = goal - (big_used * 5)

    if a >= remaining_length:
        print(remaining_length)
    else:
        print(-1)

main()
