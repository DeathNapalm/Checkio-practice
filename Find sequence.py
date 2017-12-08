def isSequenceInside(array):
    i = 0
    sequence = ""
    while i < len(array):
        if sequence == "" or str(array[i]) == sequence[-1]:
            sequence += str(array[i])
            if len(sequence) > 3:
                return True
        else:
            sequence = str(array[i])
            if len(array) - i < 4:
                return False
        i += 1


def checkio(matrix):
    # Checking horizontally
    for row in matrix:
        if isSequenceInside(row): return True

    # Checking vertically
    for index in range(0, len(matrix)):
        column = [row[index] for row in matrix]
        if isSequenceInside(column): return True

    # Checking diagonals
    for i in range(len(matrix) - 3):
        diagonal1 = [matrix[j + i][j] for j in range(len(matrix) - i)]
        if isSequenceInside(diagonal1): return True
        diagonal2 = [matrix[j][j + i] for j in range(len(matrix) - i)]
        if diagonal1 != diagonal2 and isSequenceInside(diagonal2): return True
        diagonal3 = [matrix[len(matrix) - 1 - j - i][j] for j in range(len(matrix) - i)]
        if isSequenceInside(diagonal3): return True
        diagonal4 = [matrix[len(matrix) - 1 - j][j + i] for j in range(len(matrix) - i)]
        if diagonal3 != diagonal4 and isSequenceInside(diagonal4): return True

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([[2, 6, 2, 2, 7, 6, 5], [3, 4, 8, 7, 7, 3, 6], [6, 7, 3, 1, 2, 4, 1], [2, 5, 7, 6, 3, 2, 2],
                    [3, 4, 3, 2, 7, 5, 6], [8, 4, 6, 5, 2, 9, 7], [5, 8, 3, 1, 3, 7, 8]]) == False