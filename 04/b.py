def main():
    # gets data from the a.txt file in the same directory
    file = open("a.txt", "r")

    total_score = 0

    # reads the data from the file by line
    for line in file:
        # get elf values by splits line at the comma, then at hyphen
        elf_1 = line.split(",")[0]
        elf_1_min = int(elf_1.split("-")[0])
        elf_1_max = int(elf_1.split("-")[1])
        elf_2 = line.split(",")[1]
        elf_2_min = int(elf_2.split("-")[0])
        elf_2_max = int(elf_2.split("-")[1])

        # get range of elf_1 and elf_2
        elf_1_range = range(elf_1_min, elf_1_max + 1)
        elf_2_range = range(elf_2_min, elf_2_max + 1)

        # see if elf_1_range and elf_2_range overlap
        if set(elf_1_range).intersection(elf_2_range):
            total_score += 1

    # print score
    print(total_score)

    # close the file
    file.close()


if __name__ == "__main__":
    main()
