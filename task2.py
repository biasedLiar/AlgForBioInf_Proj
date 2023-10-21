from substitutionDP import DPTable
import matplotlib.pyplot as plt




# Create tree structure
a = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"
PERCENT = 10
table = DPTable(PERCENT/100, a)
lines = open("s_3_sequence_1M.txt").read().splitlines()


lengthSum = 0

lengthList = []
lenList = []

lineLength = len(lines[1])
for i in range(lineLength+1):
    lengthList.append(0)


print()
for line in lines[:1000]:
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

plt.hist(lenList, bins=50)
plt.show()
