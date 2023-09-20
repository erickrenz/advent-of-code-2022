def main():
    # gets data from the a.txt file in the same directory
    file = open("a.txt", "r")

    total_score = 0

    # reads the data from the file by line
    for line in file:
        # calculates the line length, minus 1 for the newline character
        line_length = len(line) - 1

        # split the backpack into two compartments
        first_half = line[: line_length // 2]
        second_half = line[line_length // 2 :]

        # for each letter in the first half, see if the letter is in the second half
        for letter in first_half:
            if letter in second_half:
                value = get_letter_value(letter)
                total_score += value
                break

    # print score
    print(total_score)

    # close the file
    file.close()


# function that inputs a char and returns the corresponding ascii integer value\
def get_letter_value(char: str) -> int:
    ascii_value = ord(char)

    # lowercase letters have values from 1-26
    if ascii_value >= 97 and ascii_value <= 122:
        return ascii_value - (97 - 1)  # 96

    # uppercase letters have values from 27-52
    if ascii_value >= 65 and ascii_value <= 90:
        return ascii_value - (65 - 27)  # 38

    return 0


if __name__ == "__main__":
    main()
