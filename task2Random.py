from substitutionDP import DPTable
import matplotlib.pyplot as plt
import random



# Create tree structure
a = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"
PERCENT = 10
table = DPTable(PERCENT/100, a)


lengthSum = 0

lengthList = []
lenList = []

numRandLines = 1000000
lines=[]
update = 2
lineLength = 50
for i in range(numRandLines):
    myString = ""
    for jA in range(lineLength):
        myString += ["A", "C", "G", "T"][random.randint(0, 3)]
    lines.append(myString)


for i in range(lineLength+1):
    lengthList.append(0)


print()
for line in lines[:10000]:
    col = table.GASolve(line)
    matchString = table.getCommonString()
    #print(matchString)
    lengthSum += len(matchString)
    lengthList[len(matchString)] += 1
    lenList.append(len(matchString))

#lengthList = [length/len(lines) for length in lengthList]
print("Sequences found: " + str((len(lines)-lengthList[0])))
print("Sequence lengths after adapter match removal:")
for length in range(len(lengthList)):
    if length != 0 and lengthList[length] != 0:
        print("Length: " + str(lineLength - length) + ", num: " + str(lengthList[length]))
print(lengthList)

plt.hist(lenList, bins=range(51))
plt.show()
