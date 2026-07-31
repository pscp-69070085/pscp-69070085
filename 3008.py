'''พื้นที่ของสามเหลี่ยมใดๆที่มีความยาวด้านทั้ง 3 ด้าน เป็น a, b และ c'''
import math as m
def main():
    '''main'''
    a = float(input())
    b = float(input())
    c = float(input())
    s =(a+b+c)/2
    area = m.sqrt((s*(s-a)*(s-b)*(s-c)))
    print(f"{area:.3f}")

main()
