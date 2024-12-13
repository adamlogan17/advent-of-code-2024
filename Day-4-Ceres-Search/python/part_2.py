from part_1 import read_input

def find_word(word_search, word):
    total = 0

    for j in range(1, (len(word_search)-1)):
        for i in range(1, (len(word_search[j])-1)):
            if word_search[j][i] == 'A':
                x = ['M','S']
                if ((word_search[j+1][i-1] in x) and 
                    (word_search[j+1][i+1] in x) and 
                    (word_search[j+1][i-1] in x) and 
                    (word_search[j-1][i+1] in x) and 
                    (word_search[j-1][i-1] in x) and 
                    (word_search[j+1][i-1] != word_search[j-1][i+1]) and
                    (word_search[j+1][i+1] != word_search[j-1][i-1])):
                    total+=1
    return total

if __name__ == '__main__':
    word_search = read_input()
    word_to_find = 'MAS'
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