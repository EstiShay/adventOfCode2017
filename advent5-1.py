import csv

adventFile = open('advent5Data.csv')
adventReader = csv.reader(adventFile)
adventData = list(adventReader)


def getOut1(maze):
    #Create an array of the values from the csv so I can modify the values
    allSteps = []
    for row in maze:
        allSteps.append(int(row[0]))

    moves = 0
    position = 0

    while position < len(maze):
        myMove = allSteps[position]
        allSteps[position] += 1
        position += myMove
        moves += 1

    print("It took "+str(moves)+" moves to escape the labyrinth")

getOut1(adventData)
