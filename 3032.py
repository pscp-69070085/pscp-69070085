'''scoreexam'''
def main():
    '''main'''
    num = int(input())
    scores = []
    for _ in range(num):
        scores.append(int(input()))
        maxscore = max(scores)
        showtop = scores.count(maxscore)
    print(maxscore)
    print(showtop)

main()
