'''Taxi'''
import math as m
def main():
    '''main'''
    kilo = float(input())

    if not kilo:
        print(0)
    elif kilo <= 1:
        print(35)
    elif 1 < kilo <= 10:
        kilo -= 1
        print(m.floor(kilo)*5 + 35)
    elif kilo > 10:
        kilo -= 10
        print(m.floor(kilo)*8 + 80)

main()
