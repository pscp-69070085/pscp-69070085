'''เขียนโปรแกรมรับชื่อและนามสกุลของผู้ใช้ แล้วพิมพ์ข้อความ "Hello name and surname"
พร้อมกับชื่อแฝงที่มาจากตัวอักษร 2 ตัวแรกของชื่อและนามสกุล'''
def main():
    '''main'''
    name = input()
    surname = input()
    print("Hello", name , surname)
    print(name[0:2]+surname[0:2])

main()
