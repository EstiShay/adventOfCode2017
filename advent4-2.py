import csv

adventFile = open('advent4Data.txt')
adventReader = csv.reader(adventFile)
adventData = list(adventReader)

def passphrases2(passList):
    valid = 0

    for entry in passList:
        entryWords = entry[0].split(" ")
        index1 = 0
        index2 = 1
        check = True

        while check == True and index2 < len(entryWords):
            index3 = index2
            while check == True and index3 < len(entryWords):
                isAnagram = anagramCheck(entryWords[index1], entryWords[index3])
                if isAnagram:
                    check = False
                else:
                    index3 += 1

            index1 += 1
            index2 += 1

            if index2 == len(entryWords)-1 and check == True:
                valid += 1
                check = False

    print("There are "+str(valid)+" valid passphrases")


def anagramCheck(word1, word2):
    word1List = list(word1)
    word1List.sort()
    word2List = list(word2)
    word2List.sort()
    if (word1List == word2List):
        return True
    else:
        return False


passphrases2(adventData)
