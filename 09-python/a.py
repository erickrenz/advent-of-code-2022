""" Advent of Code 2022 | Day 9 | Part 1 """

# gets data from the data.txt file in the same directory
with open("data.txt", "r", encoding="utf-8") as file:

    # get data from the file
    data = file.read().splitlines()

    # set the starting positions
    H = [0, 0]
    T = [0, 0]
    previous_T = [[0, 0]]

    # loop through all lines in the file
    for line in data:

        # split the line at the space
        letter = line.split(" ")[0]
        number = int(line.split(" ")[1])

        for moves in range(number):
            if letter == "U":
                H[1] += 1
                if abs(H[1] - T[1]) > 1 or abs(H[0] - T[0]) > 1:
                    T = [H[0], H[1] - 1]
                    if T not in previous_T:
                        previous_T.append(T)
            elif letter == "D":
                H[1] -= 1
                if abs(H[1] - T[1]) > 1 or abs(H[0] - T[0]) > 1:
                    T = [H[0], H[1] + 1]
                    if T not in previous_T:
                        previous_T.append(T)
            elif letter == "R":
                H[0] += 1
                if abs(H[1] - T[1]) > 1 or abs(H[0] - T[0]) > 1:
                    T = [H[0] - 1, H[1]]
                    if T not in previous_T:
                        previous_T.append(T)
            elif letter == "L":
                H[0] -= 1
                if abs(H[1] - T[1]) > 1 or abs(H[0] - T[0]) > 1:
                    T = [H[0] + 1, H[1]]
                    if T not in previous_T:
                        previous_T.append(T)

    # print the number of positions
    print(len(previous_T))
