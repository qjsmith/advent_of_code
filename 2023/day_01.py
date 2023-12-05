# --- Day 1: Trebuchet?! ---

def main():
    file_location = f"./inputs/day_01_input.txt"
    calibration_value_sum = get_sum_calibration_document(file_location)
    print(f"the sum of the calibration document is: {calibration_value_sum}")


# The following function is for Day 1 Part 2
def convert_word_numbers_to_int(line_string):
    number_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    for key, value in number_dict.items():
        while key in line_string:
            index = line_string.find(key)
            # word numbers can overlap. Replace second letter of number with int
            line_string = f'{line_string[:index+1]}{value}{line_string[index + 2:]}'
    return line_string


def document_line_to_number(line_string):
    number_indexes = [i for i in range(0, len(line_string)) if line_string[i].isdigit()]
    value = f"{line_string[number_indexes[0]]}{line_string[number_indexes[-1]]}"
    value = int(value)
    return value


def get_sum_calibration_document(file_location):
    line_values = []
    with open(file_location) as file:
        for line in file:
            line = convert_word_numbers_to_int(line)
            line_values.append(document_line_to_number(line))

    return sum(line_values)


main()
