import random
import numpy as np
import matplotlib.pyplot as plt
from suffixTree import TreeNode

# Create tree structure
a = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"
root = TreeNode("")
nodes = [root]
root.createSuffixTreeFor(a)
root.printTree()
lines = open("s_3_sequence_1M.txt").read().splitlines()


lengthSum = 0

lengthList = []
lenList = []

lineLength = len(lines[1])
print()
for i in range(lineLength+1):
    lengthList.append(0)


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

#lengthList = [length/len(lines) for length in lengthList]
print("Sequences found: " + str((len(lines)-lengthList[0])))
print("Sequence lengths after adapter match removal:")
for length in range(len(lengthList)):
    if length != 0 and lengthList[length] != 0:
        print("Length: " + str(lineLength - length) + ", num: " + str(lengthList[length]))
print(lengthList)

plt.hist(lenList, bins=50)
plt.show()
