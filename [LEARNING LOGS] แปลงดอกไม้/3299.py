"""แปลงดอกไม้"""
import math as m
def main():
    """main"""
    l, n = map(int, input().split())
    count = 1
    floor = 0
    multiplier = 1
    while count <= n:
        count += multiplier
        multiplier += 1
        floor += 1
    print(m.ceil(floor / l))

main()
