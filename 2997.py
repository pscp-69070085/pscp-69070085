'''คำนวณระดับทักษะของผู้เล่นหรือผู้เข้าแข่งขันในเกมที่มีลักษณะผลรวมเป็นศูนย์ (zero sum game)'''
def main():
    '''main'''
    RA = int(input())
    RB = int(input())
    AB = input()
    if AB == "A":
        EA = 1/(1+(10**((RB-RA)/400)))
        print(f"{EA:.2f}")
    elif AB == "B":
        EB = 1/(1+(10**((RA-RB)/400)))
        print(f"{EB:.2f}")

main()
