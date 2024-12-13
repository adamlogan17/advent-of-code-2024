
def read_input(input_dir='../input.txt'):
    all_text = []

    with open(input_dir, 'r') as file:
        for line in file:
            all_text.append(line)
    return all_text

def find_word(word_search, word):
    total = 0
    horizontal_total = 0
    vertical_total = 0
    diagonal_total = 0
    length_of_word = len(word)

    for j in range(len(word_search)):
        for i in range(len(word_search[j])):
            horizontal = word_search[j][i:i+length_of_word]
            if word == horizontal or word == horizontal[::-1]:
                horizontal_total += 1

            vertical = ''
            try:
                for z in range(length_of_word):
                    vertical += word_search[j+z][i]
                if word == vertical or word == vertical[::-1]:
                    vertical_total += 1
            except:
                pass

            diagonal_right = ''
            diagonal_left = ''
            for z in range(length_of_word):
                try:
                    diagonal_right += word_search[j+z][i+z]
                except:
                    pass
                try:
                    diagonal_left += word_search[j+z][i-z]
                except:
                    pass
            if word == diagonal_left or word == diagonal_left[::-1]:
                diagonal_total += 1
            # Need to keep these separate so it can count twice if one element has a match both left and right
            if word == diagonal_right or word == diagonal_right[::-1]:
                diagonal_total += 1
    return horizontal_total + vertical_total + diagonal_total

if __name__ == '__main__':
    word_search = read_input()
    word_to_find = 'XMAS'
    short_word_search = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]

    print(find_word(word_search, word_to_find))