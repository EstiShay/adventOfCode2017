import csv

adventFile = open('advent2Data.csv')
adventReader = csv.reader(adventFile)
adventData = list(adventReader)

def checksum(spreadsheet):
    output = 0
    for row in spreadsheet:
        big = 0
        small = 10000

        rowData = row[0].split()

        for num in rowData:
            num = int(num)
            if num > big:
                big = num
            if num < small:
                small = num

        diff = big - small

        output += diff

    print(output)

checksum(adventData)
