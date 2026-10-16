"""PickThem"""
import json

def main():
    """main"""
    data = json.loads(input())
    evens = [x for x in data if isinstance(x, int) and not isinstance(x, bool) and not x % 2]
    if evens:
        for x in evens:
            print(x)
    else:
        print("Nope")
main()
