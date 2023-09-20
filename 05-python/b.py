def main():
    # gets data from the a.txt file in the same directory
    file = open("a.txt", "r")

    stack = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    stack[1] = ["N", "R", "G", "P"]
    stack[2] = ["J", "T", "B", "L", "F", "G", "D", "C"]
    stack[3] = ["M", "S", "V"]
    stack[4] = ["L", "S", "R", "C", "Z", "P"]
    stack[5] = ["P", "S", "L", "V", "C", "W", "D", "Q"]
    stack[6] = ["C", "T", "N", "W", "D", "M", "S"]
    stack[7] = ["H", "D", "G", "W", "P"]
    stack[8] = ["Z", "L", "P", "H", "S", "C", "M", "V"]
    stack[9] = ["R", "P", "F", "L", "W", "G", "Z"]

    # reads the data from the file by line
    for line in file:
        # if the line does not begin with the word "move", continue
        if not line.startswith("move"):
            continue

        # get the values from each line
        quantity = int(line.split()[1])
        start = int(line.split()[3])
        end = int(line.split()[5])

        # transition stack
        cratemover = []

        # loop for the quantity of times the move is to be made
        for moves in range(quantity):
            crate = stack[start].pop()
            cratemover.append(crate)

        for moves in range(quantity):
            crate = cratemover.pop()
            stack[end].append(crate)

    # print the final stack
    for row in stack:
        print(row)

    # close the file
    file.close()


if __name__ == "__main__":
    main()
