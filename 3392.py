"""Array ฮาเฮ"""
def main():
    """main"""
    nums = []
    for i in range(1, 4):
        nums.append(int(input()))
        print(f"Input number {i} stored.")

    while True:
        choice = int(input())
        if not choice :
            break
        if choice == 1:
            print("Original order:", *nums)
        elif choice == 2:
            print("Descending order:", *sorted(nums, reverse=True))
        elif choice == 3:
            print("Ascending order:", *sorted(nums))
main()
