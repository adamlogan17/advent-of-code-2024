from part_1 import read_input
import re

def filter_text(text, start_char, end_char, regex=r'.*', discard_match_chars=False):
    filtered_text = []
    current_filtered_text = ''
    reached_start = False
    conditional_str = ''
    reached_start_conditional = False
    add_operator = True

    for i in range(len(text)):
        char = text[i]
        if char == 'd':
            try:
                if text[i:i+5] == "don't":
                    add_operator = False
                elif text[i:i+2] == "do":
                    add_operator = True
            except:
                pass

        if char == start_char:
            current_filtered_text = ''
            reached_start = True
        elif char == end_char and reached_start:
            if discard_match_chars:
                current_filtered_text = current_filtered_text[1:]
            else:
                current_filtered_text += char
            reached_start = False
            if re.match(regex, current_filtered_text) and add_operator:
                filtered_text.append(current_filtered_text)
        
        if reached_start:
            current_filtered_text += char
    return filtered_text

def extract_operations(text):
    regex = r"mul\([0-9]*,[0-9]*\)"
    operations = filter_text(text, 'm', ')' , regex=regex)
    total = 0

    for operation in operations:
        num_1 = filter_text(operation, '(', ',', regex=r'[0-9]*', discard_match_chars=True)[0]
        num_2 = filter_text(operation, ',', ')', regex=r'[0-9]*', discard_match_chars=True)[0]
        total += int(num_1) * int(num_2)

    return total


if __name__ == '__main__':
    corrupted_memory = read_input()
    short_corrupted_memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    total = extract_operations(corrupted_memory)

    print(total)