# gets data from the data.txt file in the same directory
with open("data.txt", "r", encoding="utf-8") as file:

    # get data from the file
    data = file.read().splitlines()

    # counts the trees that are visible | 9081 Total Trees
    visible_trees = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            # check if tree is in first or last row
            if row == 0 or row == len(data) - 1:
                visible_trees += 1
                continue

            # check if tree is in first or last column
            if col == 0 or col == len(data[row]) - 1:
                visible_trees += 1
                continue

            # get current tree
            current_tree = data[row][col]

            # check if tree is visible from the left
            if max(data[row][:col]) < current_tree:
                visible_trees += 1
                continue

            # check if tree is visible from the right
            if max(data[row][col + 1 :]) < current_tree:
                visible_trees += 1
                continue

            # check if tree is visible from the top
            top = [data[r][col] for r in range(0, row)]
            if max(top) < current_tree:
                visible_trees += 1
                continue

            # check if tree is visible from the bottom
            bottom = [data[r][col] for r in range(row + 1, len(data))]
            if max(bottom) < current_tree:
                visible_trees += 1
                continue

    # print result
    print(visible_trees)
