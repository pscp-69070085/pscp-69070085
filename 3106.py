'''ATM'''
def main():
    '''main'''
    money = int(input())

    if not money % 100 and 20000 >= money >= 100:
        if money >= 1000:
            print(f"1000 = {money//1000}")
        if money%1000 >= 500:
            print(f"500 = {money%1000//500}")
        if money%500 >= 100:
            print(f"100 = {money%500//100}")
    else:
        print("ERROR")

main()
