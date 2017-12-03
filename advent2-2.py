import csv

adventFile = open('advent2Data.csv')
adventReader = csv.reader(adventFile)
adventData = list(adventReader)

def checksum2(spreadsheet):
    output = 0
    #Look at each row
    for row in spreadsheet:
        index1 = 0
        index2 = 1
        divisor = 0
        rowData = row[0].split()

        while index1 < len(rowData)-1:
            #Iterate over subsequent numbers in the list
            index3 = index2

            j = 1
            #Condition to end while loop comparing numbers
            while j < (len(rowData)-index1):
                data1 = int(rowData[index1])
                data3 = int(rowData[index3])
                if data1 % data3 == 0 or data3 % data1 == 0:
                    divisor1 = data1 / data3
                    divisor2 = data3 / data1
                    if divisor1 >= 1:
                        divisor = divisor1
                        #End both loops when divisor found for that row
                        j = 1000
                        index1 = 1000
                    if divisor2 >= 1:
                        divisor = divisor2
                        #End both loops when divisor found for that row
                        j = 1000
                        index1 = 1000
                index3 += 1
                #Move to the next number in the list
                j += 1
                #Move forward in while loop

            index1 += 1
            #Move first number forward in list
            index2 += 1
            #Move starting position of second number forward in list

        output += divisor

    print(output)

checksum2(adventData)
