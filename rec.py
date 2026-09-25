"""PrimeNumber"""
def main():
    """PrimeNumber"""
    num = input().split()
    start = int(num[0])
    end = int(num[1])
    prime = []
    for n in range(start, end+1):
        if n <= 1:
            continue
        isprime = True
        for p in range(2,n):
            if not n % p:
                isprime = False
                break
        if isprime:
            prime.append(n)
    if prime:
        print(*prime)
    print("Total primes:" , len(prime))
main()