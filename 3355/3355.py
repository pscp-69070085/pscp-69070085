"""[LEARNING LOGS] Shorten"""
def main():
    """main"""
    nums = []
    while True:
        x = int(input())
        if x == -1:
            break
        nums.append(x)

    parts = []
    i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if j == i:
            parts.append(str(nums[i]))
        else:
            parts.append(f"{nums[i]}-{nums[j]}")
        i = j + 1

    print(", ".join(parts))
main()
