from collections import defaultdict


def main():
    # gets data from the data.txt file in the same directory
    file = open("data.txt", "r", encoding="utf-8")

    # variable that stores the minimum size of the file
    minimum_size = 0

    # variable that stores the previous directories
    path, dirs = [], defaultdict(int)

    # reads the data from the file by line
    for line in file:
        # remove the \n at the end of the line
        line = line.strip()

        # split line at space
        command = line.split(" ")

        # lines starting with "$" are commands
        if command[0] == "$":
            if command[1] != "cd":
                continue

            # update the pwd variable
            if command[2] == "..":
                # remove the last item in array
                path.pop()
            else:
                # add the directory to the array
                path.append(command[2])

        # lines starting with "dir" are directories
        elif not line.startswith("dir"):
            # loop through the directories and add the size of the files
            for folder in range(len(path)):
                dirs[tuple(path[: folder + 1])] += int(command[0])

    # calculate the minimum required size needed for deletion
    minimum_required = 30000000 - (70000000 - dirs[("/",)])

    # find the minimum size of the directory
    for size in dirs.values():
        if size < minimum_required:
            continue
        if size < minimum_size or minimum_size == 0:
            minimum_size = size

    # print result
    print(minimum_size)

    # close the file
    file.close()


if __name__ == "__main__":
    main()
