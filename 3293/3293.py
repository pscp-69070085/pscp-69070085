"""BigFrame"""
def main():
    """main"""
    massage = [input() for _ in range(5)]
    long = max(len(w) for w in massage)
    print("*"*(long + 4))
    for i in massage:
        print(f"* {i:<{long}} *")
    print("*"*(long + 4))

main()
