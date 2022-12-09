""" Advent of Code 2022 | Day 9 | Part 1 """

# gets data from the data.txt file in the same directory
with open("data.txt", "r", encoding="utf-8") as file:

    # get data from the file
    data = file.read().splitlines()

    # set the starting positions
    Knot = [
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
    ]
    previous_tails = ["1000:1000"]

    # loop through all lines in the file
    for line in data:

        # split the line at the space
        letter = line.split(" ")[0]
        number = int(line.split(" ")[1])

        for moves in range(number):

            match letter:
                case "U":
                    Knot[0][1] += 1
                case "D":
                    Knot[0][1] -= 1
                case "R":
                    Knot[0][0] += 1
                case "L":
                    Knot[0][0] -= 1

            for n in range(1, len(Knot)):
                if (
                    abs(Knot[n][0] - Knot[n - 1][0]) > 1
                    or abs(Knot[n][1] - Knot[n - 1][1]) > 1
                ):
                    if Knot[n - 1][0] > Knot[n][0]:
                        Knot[n][0] += 1
                    elif Knot[n - 1][0] < Knot[n][0]:
                        Knot[n][0] -= 1

                    if Knot[n - 1][1] > Knot[n][1]:
                        Knot[n][1] += 1
                    elif Knot[n - 1][1] < Knot[n][1]:
                        Knot[n][1] -= 1

            # see if 9 is in the previous tails list
            string = f"{Knot[9][0]}:{Knot[9][1]}"
            if string not in previous_tails:
                previous_tails.append(string)

    # print the number of positions
    print(len(previous_tails))
