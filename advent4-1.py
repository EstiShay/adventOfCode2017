import csv

adventFile = open('advent4Data.csv')
adventReader = csv.reader(adventFile)
adventData = list(adventReader)

def passphrases1(passList):
    valid = 0
    invalid = 0

    for entry in passList:
        entryWords = entry[0].split(" ")
        index1 = 0
        index2 = 1
        check = True

        while check == True and index2 < len(entryWords):
            index3 = index2
            while check == True and index3 < len(entryWords):
                if entryWords[index1] == entryWords[index3]:
                    check = False
                    invalid += 1
                else:
                    index3 += 1

            index1 += 1
            index2 += 1

            if index2 == len(entryWords)-1 and check == True:
                valid += 1

    print("There are "+str(valid)+" valid and "+str(invalid)+" invalid passphrases.")

passphrases1(adventData)
