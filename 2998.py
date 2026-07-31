'''โปรแกรมรับตัวเลข 4 ตัวจากผู้ใช้ตามลำดับ q1, q2, p1, p2'''
import math as m
def main():
    '''main'''
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())
    distance = m.sqrt(((q1-p1)**2)+((q2-p2)**2))
    print(distance)

main()
