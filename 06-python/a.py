def main():
    # gets data from the data.txt file in the same directory
    file = open("data.txt", "r", encoding="utf-8")

    signal = file.readline()

    letters = []

    # reads the data from the file by line
    for letter in signal:
        letters.append(letter)

    # print(f"Letters: {len(letters)}")

    for n in range(3, len(letters)):

        last_four_letters = letters[n - 3 : n + 1]

        # see if all four letters are different
        if (
            last_four_letters[0] != last_four_letters[1]
            and last_four_letters[0] != last_four_letters[2]
            and last_four_letters[0] != last_four_letters[3]
            and last_four_letters[1] != last_four_letters[2]
            and last_four_letters[1] != last_four_letters[3]
            and last_four_letters[2] != last_four_letters[3]
        ):
            print(last_four_letters)
            # print final location, account for zero indexing of array
            print(f"Location: {n + 1}")
            break

    # close the file
    file.close()


if __name__ == "__main__":
    main()
