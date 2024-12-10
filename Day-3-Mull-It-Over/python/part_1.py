
import re


def read_input(input_dir='../input.txt'):
    all_text = ''

    with open(input_dir, 'r') as file:
        for line in file:
            all_text += line
    return all_text

def filter_text(text, start_char, end_char, regex=r'.*', discard_match_chars=False):
    filtered_text = []
    current_filtered_text = ''
    reached_start = False

    for char in text:
        if char == start_char:
            current_filtered_text = ''
            reached_start = True
        elif char == end_char and reached_start:
            if discard_match_chars:
                current_filtered_text = current_filtered_text[1:]
            else:
                current_filtered_text += char
            reached_start = False
            if re.match(regex, current_filtered_text):
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
    short_corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    total = extract_operations(corrupted_memory)

    print(total)