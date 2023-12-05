# --- Day 2: Cube Conundrum ---

import re


def main():
    # parse line
    file_location = f"./inputs/day_02_input.txt"

    # part 1
    sum_of_game_numbers = get_sum_of_games(file_location)
    print(f'sum of the game numbers that are possible: {sum_of_game_numbers}')

    # part 2
    sum_of_cubes = get_sum_of_powers(file_location)
    print(f'sum of the min block cubed: {sum_of_cubes}')


def get_sum_of_powers(file_location):
    cubes_list = []

    with open(file_location) as file:
        for line in file:

            blue_counts = re.findall(r"(\d+) blue", line)
            if blue_counts:
                blue_counts = list(map(int, blue_counts))
                blue_largest_num = max(blue_counts)

            red_counts = re.findall(r"(\d+) red", line)
            if red_counts:
                red_counts = list(map(int, red_counts))
                red_largest_num = max(red_counts)

            green_counts = re.findall(r"(\d+) green", line)
            if green_counts:
                green_counts = list(map(int, green_counts))
                green_largest_num = max(green_counts)

            cubes_list.append(blue_largest_num*red_largest_num*green_largest_num)
    return sum(cubes_list)


def get_sum_of_games(file_location):
    game_numbers = []

    red_max = 12
    green_max = 13
    blue_max = 14

    with open(file_location) as file:
        for line in file:

            blue_counts = re.findall(r"(\d+) blue", line)
            if blue_counts:
                blue_counts = list(map(int, blue_counts))
                blue_largest_num = max(blue_counts)
                blue_lower_than_max = blue_largest_num <= blue_max
            else:
                blue_lower_than_max = True

            red_counts = re.findall(r"(\d+) red", line)
            if red_counts:
                red_counts = list(map(int, red_counts))
                red_largest_num = max(red_counts)
                red_lower_than_max = red_largest_num <= red_max
            else:
                red_lower_than_max = True

            green_counts = re.findall(r"(\d+) green", line)
            if green_counts:
                green_counts = list(map(int, green_counts))
                green_largest_num = max(green_counts)
                green_lower_than_max = green_largest_num <= green_max
            else:
                green_lower_than_max = True

            if blue_lower_than_max and red_lower_than_max and green_lower_than_max:
                game_number = re.findall(r"(\d+):", line)[0]
                game_numbers.append(game_number)

    game_numbers = list(map(int, game_numbers))
    return sum(game_numbers)


main()
