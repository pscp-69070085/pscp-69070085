'''SurprisingVote'''
def main():
    '''main'''
    totalscore = float(input())
    highscore = float(input())
    totalscore -= highscore
    second = 0
    last = 0

    if totalscore >= highscore:
        second = highscore
        last = totalscore-second
    elif totalscore < highscore:
        second = totalscore
        last = 0

    if highscore - last > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
