from part_1 import read_input, transform_to_reports

def check_safety(report, problem_dampener=0, remove_limit=1, increased_last=False):
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
            if problem_dampener < remove_limit:
                # Need 2, to deal with the possibility of the very first 
                remove_current = list(report)
                del remove_current[i]

                remove_previous = list(report)
                del remove_previous[i - 1]

                # This is to deal with change in increase/decrease caused by the first element e.g. [87, 85, 86, 89, 92, 94, 97]
                if i > 1:
                    remove_2_previous = list(report)
                    del remove_2_previous[i - 2]
                    previous_by_2 = check_safety(remove_2_previous, problem_dampener + 1)
                else:
                    previous_by_2 = False

                current = check_safety(remove_current, problem_dampener + 1)
                previous = check_safety(remove_previous, problem_dampener + 1)
                return current or previous or previous_by_2
            else:
                return False

    return True

if __name__ == "__main__":
    raw_input = read_input()
    reactor_reports = transform_to_reports(raw_input)

    short_reactor_reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]

    edge_cases = [[87, 85, 86, 89, 92, 94, 97], [84, 85, 86, 89, 92, 94, 95], [80, 85, 86, 89, 92, 94, 95]]

    safe = 0
    unsafe = 0

    for report in reactor_reports:
        if check_safety(report):
            safe += 1
        else:
            unsafe += 1
    print(safe, unsafe)