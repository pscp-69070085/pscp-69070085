'''bill'''
def main():
    '''vat7'''
    num = int(input())
    service = num * 0.10
    service = max(50, min(service, 1000))
    paid = (num + service) * 1.07
    print(f"{paid:.2f}")

main()
