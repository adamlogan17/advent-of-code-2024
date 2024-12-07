
def read_input(input_dir='../input.txt'):
    lines = []

    with open(input_dir, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines

def transform_to_reports(input):
    reports = []

    for line in input:
        reports.append(list(map(int, line.split())))

    return reports

def check_safety(report):
    difference = 0
    increase = False
    decrease = False

    for i in range(1, len(report)):
        level = report[i]
        prev_level = report[i - 1]
        difference = level - prev_level

        # Checks if it is an increase or decrease
        if difference > 0:
            increase = True
        elif difference < 0:
            # Can use 'abs' to get the same effect but it is to demonstrate this for languages that do not have 'abs'
            difference = difference * -1
            decrease = True
        if (increase and decrease) or (difference < 1 or difference > 3):
            return False

    return True


if __name__ == '__main__':
    raw_input = read_input()
    reactor_reports = transform_to_reports(raw_input)

    short_reactor_reports = [
        # [7, 6, 4, 2, 1],
        # [1, 2, 7, 8, 9],
        # [9, 7, 6, 2, 1],
        # [1, 3, 2, 4, 5],
        # [8, 6, 4, 4, 1],
        # [1, 3, 6, 7, 9],
        # [84, 85, 86, 89, 92, 94, 93]
        [85, 86, 89, 92, 94, 97]
    ]

    safe = 0
    unsafe = 0

    for report in short_reactor_reports:
        if check_safety(report):
            safe += 1
        else:
            unsafe += 1

    print (safe, unsafe)