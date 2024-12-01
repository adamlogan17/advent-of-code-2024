from copy import deepcopy

def read_input():
    left_col = []
    right_col = []

    with open('input.txt', 'r') as file:
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
    left_col, right_col = read_input()
    
    distance = calc_distance(left_col, right_col)

    print(distance)
