import part_1

def similarity_score(right_col, left_col):
    score = 0

    for i in range(len(left_col)):
        occurrences = right_col.count(left_col[i])

        score += left_col[i] * occurrences

    return score

if __name__ == '__main__':
    short_left_col = [3, 4, 2, 1, 3, 3]
    short_right_col = [4, 3, 5, 3, 9, 3]
    
    right_col, left_col = part_1.read_input()

    answer = similarity_score(right_col, left_col)

    print(answer)