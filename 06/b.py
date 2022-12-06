def main():
    # gets data from the data.txt file in the same directory
    file = open("data.txt", "r", encoding="utf-8")

    signal = file.readline()

    letters = []

    # reads the data from the file by line
    for letter in signal:
        letters.append(letter)

    # print(f"Letters: {len(letters)}")

    for n in range(13, len(letters)):

        last_fourteen_letters = str(letters[n - 13 : n + 1])

        # see if all four letters are different
        if (
            last_fourteen_letters.count(letters[n - 13]) == 1
            and last_fourteen_letters.count(letters[n - 12]) == 1
            and last_fourteen_letters.count(letters[n - 11]) == 1
            and last_fourteen_letters.count(letters[n - 10]) == 1
            and last_fourteen_letters.count(letters[n - 9]) == 1
            and last_fourteen_letters.count(letters[n - 8]) == 1
            and last_fourteen_letters.count(letters[n - 7]) == 1
            and last_fourteen_letters.count(letters[n - 6]) == 1
            and last_fourteen_letters.count(letters[n - 5]) == 1
            and last_fourteen_letters.count(letters[n - 4]) == 1
            and last_fourteen_letters.count(letters[n - 3]) == 1
            and last_fourteen_letters.count(letters[n - 2]) == 1
            and last_fourteen_letters.count(letters[n - 1]) == 1
            and last_fourteen_letters.count(letters[n]) == 1
        ):
            print(last_fourteen_letters)
            # print final location, account for zero indexing of array
            print(f"Location: {n + 1}")
            break

    # close the file
    file.close()


if __name__ == "__main__":
    main()
