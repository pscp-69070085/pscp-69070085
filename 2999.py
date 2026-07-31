'''รับค่า string เข้ามา 1 บรรทัด และแสดงค่า string นั้นในกรอบรูปสี่เหลี่ยม'''
def main():
    '''main'''
    beam = input()
    frame = "*" * (len(beam)+2)
    print(frame)
    print(f"*{beam}*")
    print(frame)

main()
