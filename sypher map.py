def recall_password(cipher_grille, ciphered_password):
    rotated = cipher_grille
    str1 = ''
    for turn in range(4):
        for i in range(len(rotated)):
            for j in range(len(rotated[i])):
                if rotated[i][j] == 'X':
                    str1 += ciphered_password[i][j]
                    # print(str1)
        rotated = tuple(zip(*rotated[::-1]))
    return str1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
