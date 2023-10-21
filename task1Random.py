import random
import numpy as np
import matplotlib.pyplot as plt
from suffixTree import TreeNode






# Create tree structure
a = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"
root = TreeNode("")
nodes = [root]
root.createSuffixTreeFor(a[::-1])
root.printTree()
lines = open("s_3_sequence_1M.txt").read().splitlines()
lineLength = len(lines[1])






lengthSum = 0
lengthList = []
lenList = []
print()

for i in range(lineLength+1):
    lengthList.append(0)

numRandLines = 1000000
lines=[]
update = 2
for i in range(numRandLines):
    myString = ""
    for j in range(lineLength):
        myString += ["A", "C", "G", "T"][random.randint(0, 3)]
    lines.append(myString)


for line in lines:
    (successful, matchString) = root.followString(line[::-1])
    if successful:
        #print(matchString)
        lengthSum += len(matchString)
        lengthList[len(matchString)] += 1
        lenList.append(len(matchString))
    else:
        lengthList[0] += 1
        lenList.append(0)

print(lengthList)

print("Sequences found: " + str((len(lines)-lengthList[0])))

plt.hist(lenList, bins=range(52))
plt.show()
