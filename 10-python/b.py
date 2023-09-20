""" Advent of Code 2022 | Day 10 | Part 2 """


def main():
    # gets data from the data.txt file in the same directory
    with open("data.txt", "r", encoding="utf-8") as file:

        # get data from the file
        data = file.read().splitlines()

        signal = 1
        current_cycle = 0
        cycle_count = 20
        strengths = 0

        crt_row = ""

        # loop through all lines in the file
        for line in range(len(data)):

            # During Cycle
            current_cycle += 1

            if len(crt_row) in (signal - 1, signal, signal + 1):
                crt_row += "X"
            else:
                crt_row += "."

            if current_cycle % 40 == 0:
                print(crt_row)
                crt_row = ""

            if current_cycle == cycle_count:
                cycle_count, strengths = increment_strengths(
                    signal, cycle_count, strengths
                )

            # After Cycle

            if str(data[line]) == "noop" or str(data[line].split(" ")[0]) != "addx":
                continue

            # addx takes 2x cycles

            current_cycle += 1

            if len(crt_row) in (signal - 1, signal, signal + 1):
                crt_row += "X"
            else:
                crt_row += "."

            if current_cycle % 40 == 0:
                print(crt_row)
                crt_row = ""

            if current_cycle == cycle_count:
                cycle_count, strengths = increment_strengths(
                    signal, cycle_count, strengths
                )

            signal += int(data[line].split(" ")[1])


def increment_strengths(signal, cycle_count, strengths):
    strengths += signal * cycle_count
    cycle_count += 40
    return cycle_count, strengths


if __name__ == "__main__":
    main()
