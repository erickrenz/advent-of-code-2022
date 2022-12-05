def main():
    # gets data from the a.txt file in the same directory
    file = open("a.txt", "r")

    words = []
    myTotalScore = 0

    # reads the data from the file by line
    for line in file:
        # splits the line at every space
        # words.append(line.split())

        elfGuess = line.split()[0]
        myGuess = line.split()[1]

        myScore = 0

        match myGuess:
            case "X":
                myScore += 0
                match elfGuess:
                    case "A":
                        myScore += 3
                    case "B":
                        myScore += 1
                    case "C":
                        myScore += 2
            case "Y":
                myScore += 3
                match elfGuess:
                    case "A":
                        myScore += 1
                    case "B":
                        myScore += 2
                    case "C":
                        myScore += 3
            case "Z":
                myScore += 6
                match elfGuess:
                    case "A":
                        myScore += 2
                    case "B":
                        myScore += 3
                    case "C":
                        myScore += 1

        myTotalScore += myScore

    # print(words[0][0])
    # print(words[2499][1])

    print(myTotalScore)

    # close the file
    file.close()


if __name__ == "__main__":
    main()
