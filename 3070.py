"""นับเลขคู่และเลขคี่"""
def main():
    """main"""
    numbers = [int(input()) for _ in range(3)]

    even_count = sum(1 for n in numbers if not n % 2)
    odd_count = sum(1 for n in numbers if n % 2)

    print(even_count)
    print(odd_count)

main()
