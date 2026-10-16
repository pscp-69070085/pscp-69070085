"""LastStand"""
import ast
def main():
    """main"""
    lst = ast.literal_eval(input())

    for num in lst:
        print(str(num)[-1])

main()
