def get_coords(peace):
    res = [-1, -1]
    check_letter = 'abcdefgh'
    check_number = '12345678'
    if peace[0] in check_letter:
        res[1] = check_letter.index(peace[0])
    if peace[1] in check_number:
        res[0] = 7 - check_number.index(peace[1])
    return tuple(res)
    

def get_coords_to_move(cord):
    res = []

    res.append((cord[0] - 2, cord[1] - 1))
    res.append((cord[0] - 1, cord[1] - 2))
    res.append((cord[0] + 1, cord[1] + 2))
    res.append((cord[0] + 2, cord[1] + 1))
    res.append((cord[0] - 1, cord[1] + 2))
    res.append((cord[0] + 1, cord[1] - 2))
    res.append((cord[0] - 2, cord[1] + 1))
    res.append((cord[0] + 2, cord[1] - 1))

    for item in res:
        if item[0] < 0 or item[0] > 7 or item[1] < 0 or item[1] > 7:
            del res[res.index(item)]

    return res


n = 8
queen = input()
coords = get_coords(queen)
coords_to_move = get_coords_to_move(coords)

desk = [['.']*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i, j) == coords:
            desk[i][j] = "Q"
        elif i == coords[0]:
            desk[i][j] = '*'
        elif j == coords[1]:
            desk[i][j] = '*'
        elif i+j == sum(coords):
            desk[i][j] = '*'
        elif i-j == coords[0] - coords[1]:
            desk[i][j] = '*'

for row in desk:
    print(' '.join(list(map(str, row))))
