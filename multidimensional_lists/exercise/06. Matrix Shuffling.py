def valid_command(data: list) -> bool:
    if tokens[0] != 'swap':
        return False
    if len(tokens) != 5:
        return False
    coordinates = [int(x) for x in tokens[1:]]
    if min(coordinates) < 0:
        return False
    x1, y1, x2, y2 = coordinates
    if max(x1, x2) > row - 1:
        return False
    if max(y1, y2) > col - 1:
        return False
    return True


def print_matrix(data: list) -> None:
    for row in data:
        print(*row, sep=' ')


row, col = map(int, input().split())
matrix = [[x for x in input().split()] for _ in range(row)]
while True:
    input_line = input()
    if input_line == 'END': break

    tokens = input_line.split()
    if valid_command(tokens):
        x1, y1, x2, y2 = [int(x) for x in tokens[1:]]
        matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
        print_matrix(matrix)

    else:
        print('Invalid input!')
