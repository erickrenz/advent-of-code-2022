# gets data from the data.txt file in the same directory
with open("data.txt", "r", encoding="utf-8") as file:

    # get data from the file
    data = file.read().splitlines()

    # counts the trees that are visible | 9081 Total Trees
    best_scenic_score = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            left_score = 0
            right_score = 0
            top_score = 0
            bottom_score = 0

            # get current tree
            current_tree = data[row][col]

            # check if tree is visible from the left
            for left in reversed(range(0, col)):
                left_score += 1
                if data[row][left] >= current_tree:
                    break

            # check if tree is visible from the right
            for right in range(col + 1, len(data[row])):
                right_score += 1
                if data[row][right] >= current_tree:
                    break

            # check if tree is visible from the top
            for top in reversed(range(0, row)):
                top_score += 1
                if data[top][col] >= current_tree:
                    break

            # check if tree is visible from the bottom
            for bottom in range(row + 1, len(data)):
                bottom_score += 1
                if data[bottom][col] >= current_tree:
                    break

            # calulate best scenic score
            scenic_score = left_score * right_score * top_score * bottom_score
            best_scenic_score = (
                scenic_score if scenic_score > best_scenic_score else best_scenic_score
            )

    # print result
    print(best_scenic_score)
