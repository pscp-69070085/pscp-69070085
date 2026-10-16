"""BusStop I"""
def main():
    """main"""
    p = int(input())
    n = int(input())
    stops = {}
    for _ in range(n):
        row = list(map(int, input().split()))
        stops[row[0]] = row[1:]

    onboard = []
    count = 0
    for s in range(1, n + 1):
        count += onboard.count(s)
        onboard = [d for d in onboard if d != s]

        for d in stops.get(s, []):
            if len(onboard) >= p:
                break
            if d > s:
                onboard.append(d)
    print(count)
main()
