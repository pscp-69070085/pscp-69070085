"""FourDirections"""
def main():
    """main"""
    text1 = input()
    mat = [[]for i in range(5)]
    for i in text1:
        if i == 'U':
            mat = x_up(mat)
        elif i == 'D':
            mat = x_down(mat)
        elif i == 'R':
            mat = x_right(mat)
        elif i == 'L':
            mat = x_left(mat)

    for i in mat:
        for j in i:
            print(j, end=' ')
        print()

def x_left(mat):
    '''left'''
    mat[0].append('  *  ')
    mat[1].append(' *   ')
    mat[2].append('*****')
    mat[3].append(' *   ')
    mat[4].append('  *  ')

    return mat

def x_right(mat):
    '''right'''
    mat[0].append('  *  ')
    mat[1].append('   * ')
    mat[2].append('*****')
    mat[3].append('   * ')
    mat[4].append('  *  ')

    return mat

def x_up(mat):
    '''up'''
    mat[0].append('  *  ')
    mat[1].append(' *** ')
    mat[2].append('* * *')
    mat[3].append('  *  ')
    mat[4].append('  *  ')

    return mat

def x_down(mat):
    '''down'''
    mat[0].append('  *  ')
    mat[1].append('  *  ')
    mat[2].append('* * *')
    mat[3].append(' *** ')
    mat[4].append('  *  ')

    return mat

main()
