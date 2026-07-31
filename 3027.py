'''กระต่ายน้อยล้อมรั้วลวดหนาม'''
def main():
    '''main'''
    width, Length, Fence = map(int, input().split())
    paid = int(input())
    area = ((width * 2) + (Length * 2)) * Fence
    print(area)
    print(area * paid)

main()
