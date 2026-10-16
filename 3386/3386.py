"""[LEARNING LOGS] Duplicate I"""
def main():
    """main"""
    m = int(input())
    n = int(input())
    group1 = {input().strip() for _ in range(m)}
    group2 = {input().strip() for _ in range(n)}

    both = sorted(group1 & group2, reverse=True)

    if both:
        for code in both:
            print(code)
    else:
        print("Nope")
main()
