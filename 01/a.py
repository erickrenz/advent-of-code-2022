def main():
    # gets data from the a.txt file in the same directory
    file = open("a.txt", "r")

    # create unknown size list of elves
    elves = []
    elves.append(0)

    currentElf = 0
    currentElfCalories = 0

    # read the file line by line
    for line in file:

        # check if line is empty
        if line == "\n":
            # if it is, add the current elf to the list
            elves.append(currentElfCalories)

            # reset for next elf
            currentElfCalories = 0
            currentElf += 1
            continue

        # get line text and convert to int
        calories = int(line.strip().split()[0])
        currentElfCalories += calories

    # find the id in elves with the most calories
    elfWithMostCalories = elves.index(max(elves))
    mostCalories = max(elves)

    print(mostCalories)

    # close the file
    file.close()


if __name__ == "__main__":
    main()
