'''โปรแกรมรับรหัสนักศึกษาตรวจสอบรหัสประจำตัวคณะสารสนเทศ '''
def main():
    '''main'''
    sid = input()
    if sid[2] == "1" and sid[3] == "6":
        print("yes")
    else:
        print("no")

main()
