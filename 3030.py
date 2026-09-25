"""Saitama"""
import math as m
def main():
    """main"""
    push = int(input())
    sit = int(input())
    squat = int(input())
    run = int(input())
    Dpush = int(input())
    Dsit = int(input())
    Drun = int(input())
    Dsquat = int(input())

    daypush = m.ceil(push / Dpush)
    daysit = m.ceil(sit / Dsit)
    daysquat = m.ceil(squat / Dsquat)
    dayrun = m.ceil(run / Drun)

    print(max(daypush, daysit, daysquat, dayrun))

main()
