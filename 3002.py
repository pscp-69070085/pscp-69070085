'''โปรแกรมเพื่อรับชื่อ นามสกุล และอายุของผู้ใช้ จากนั้นสร้างรหัสผ่านของผู้ใช้ตามเงื่อนไข'''
def main():
    '''main'''
    name = input()
    surname = input()
    age = input()
    if len(name) >= 5 and len(surname) >= 5:
        print(f"{name[0:2]}{surname[-1]}{age[-1]}")
    else :
        print(f"{name[0]}{age}{surname[-1]}")

main()
