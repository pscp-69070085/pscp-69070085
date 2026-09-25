"""หาจำนวนเฉพาะ"""
def main():
    """main"""
    s,e = map(int ,input().split())
    result = []
    for i in range(s,e+1):
        if i <= 1:
            continue
        prime = True
        for j in range(2,i):
            if not i % j :
                prime = False
                break
        if prime:
            result.append(str(i))
    if result:
        print(*result)
    print("Total primes:", len(result))

main()
