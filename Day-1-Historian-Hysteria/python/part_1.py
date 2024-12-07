from copy import deepcopy

from ...utils.python.utils import read_input

def transform_input():
    left_col = []
    right_col = []

    file = read_input()

    for line in file:
        left, right = map(int, line.split())
        left_col.append(left)
        right_col.append(right)

    return left_col, right_col

def calc_distance(left_col, right_col):
    distance = 0

    left_col.sort()
    right_col.sort()

    for i in range(len(left_col)):
        distance += abs(left_col[i] - right_col[i])

    return distance

if __name__ == "__main__":
    short_left_col = [3, 4, 2, 1, 3, 3]
    short_right_col = [4, 3, 5, 3, 9, 3]
    
    left_col, right_col = read_input()
    
    answer = calc_distance(left_col, right_col)

    print(answer)
