import numpy as np
#Global Variable
numOfRes = 10
TableForBirdView = []
TableForImmersiveView = []


def half_range(ary): 
    hightest = np.amax(ary)
    half_highest = hightest/2.0
    half_highest_range = [] 
    ary.insert(0, half_highest)
    ary.sort()
    aryIndex = ary.index(half_highest)
    if(aryIndex-1 >= 0 and aryIndex + 1 < len(ary)):
        half_highest_range.append(aryIndex-1);
        half_highest_range.append(aryIndex);
        #half_highest_range.append(ary[aryIndex-1]);
        #half_highest_range.append(ary[aryIndex+1]);
    del ary[aryIndex]
    return half_highest_range


def third_range(ary): 
    hightest = np.amax(ary)
    third_highest = round(hightest/3, 2)
    third_highest_range = []
    ary.insert(0,third_highest)
    ary.sort()
    aryIndex = ary.index(third_highest)
    if(aryIndex-1 >= 0 and aryIndex + 1 < len(ary)):
        third_highest_range.append(aryIndex-1);
        third_highest_range.append(aryIndex);
        #third_highest_range.append(ary[aryIndex-1]);
        #third_highest_range.append(ary[aryIndex+1]);
    del ary[aryIndex]
    return third_highest_range

def results(ary):   
    original_ary = ary.copy()
    original_ary.sort()
    aryLen = len(original_ary)
    print(original_ary)
    hightest = original_ary[aryLen-1]
    top_three= []
    
    for i in range(3):
        top_three.append(original_ary[aryLen-1-i])

    half_highest_range = half_range(original_ary)
    print(original_ary)
    third_highest_range = third_range(original_ary)
    print(original_ary)

    result = {"Top":hightest, "Top3": top_three, "Half": half_highest_range,"Third":third_highest_range}
   
    return result
   

def buildDict(path):
    f = open(path, "r")
    
    res = []
    tempList = []
    count = 0
    for x in f:
        if x!= '=\n':
            count += 1
            tempList.append([count, float(x)])
        else:
            count = 0
            res.append(tempList)
            tempList = []
    res.append(tempList)
    del res[0]
    return res

    
def readRes(path):
    f = open(path, "r")
    tempList = []
    for x in f:
        if x != '=\n':
            x = x.replace("Bar_", "")
            x = x.replace("\n", "")
            tempList.append(int(x))
    return tempList

#s - file from users' data
#t - file from system data, true solution
def extractRes(s, t):
    tempList = []
    tempDict = []
    tempRes = []
    for i in range(numOfRes):
        tempList = readRes("{:02d}\{}".format(i+1,s))
        tempDict = buildDict("{:02d}\{}".format(i+1,t))
        listLen = len(tempList)
        for j in range(listLen):
            userIndex = tempList[j]
            if j == 0:
                tempList[j] = tempDict[0][userIndex-1]
            elif j == 1 or j == 2 or j == 3:
                tempList[j] = tempDict[1][userIndex-1]
            elif j > 3:
                tempList[j] = tempDict[j-2][userIndex-1]
        tempRes.append(tempList)
    return tempRes


def buildTempArray(dict):
    tempList = []
    for i in range(len(dict)):
        tempList.append(dict[i][1])
    return tempList
def buildSolution(t,k):
    tempList = []
    tempDict = []
    tempDict = buildDict("{:02d}\{}".format(k+1,t))
    for i in range(len(tempDict)):
        if i == 0:
            tempDict[i].sort(key=lambda tup: tup[1])
            tempList.append(tempDict[i][len(tempDict[i])-1])
        if i == 1:
            tempDict[i].sort(key=lambda tup: tup[1])
            tempList.append(tempDict[i][len(tempDict[i])-1])
            tempList.append(tempDict[i][len(tempDict[i])-2])
            tempList.append(tempDict[i][len(tempDict[i])-3])
        if i == 2:
            tempDict[i].sort(key=lambda tup: tup[1])
            tempArray = buildTempArray(tempDict[i])
            tempKey = half_range(tempArray)
            tempList.append(tempDict[i][tempKey[0]])
            tempList.append(tempDict[i][tempKey[1]])
        if i == 3:
            tempDict[i].sort(key=lambda tup: tup[1])
            tempArray = buildTempArray(tempDict[i])
            tempKey = third_range(tempArray)
            tempList.append(tempDict[i][tempKey[0]])
            tempList.append(tempDict[i][tempKey[1]])            
    return tempList

def extractFinalSolution(s, t, k):
    tempAns = extractRes(s, t)
    tempSolution = []
    for i in range(numOfRes):
        tempSolution.append(buildSolution(t, i))
    
    f = open(k,"a")
    f.write("The following data can be interpreted as:\n")
    f.write("[i, j] @i - id number of each bar; j - height of the bar with this id;\n")
    f.write("Each block (separated by two ====== lines) represented one user's choices and correct solutions:\n")
    f.write("The first line: User's choice:\n")
    f.write("@1st [i, j] - Highest bar\n")
    f.write("@2nd, 3rd, 4th [i, j] - Top 3 bars\n")
    f.write("@5th [i, j] - 1/2 highest bar\n")
    f.write("@6th [i, j] - 1/3 highest bar\n")
    f.write("\n")
    f.write("The second line: Correct solution:\n")
    f.write("@1st [i, j] - Highest bar\n")
    f.write("@2nd, 3rd, 4th [i, j] - Top 3 bars\n")
    f.write("@5th, 6th [i, j] - 1/2 highest bar (range values, as long as the user's choice is between j_5 and j_6, we consider the choice is right)\n")
    f.write("@7th, 8th [i, j] - 1/3 highest bar (the same as above)\n")
    f.write("\n")
    f.write("================================================================")
    for j in range(numOfRes):
        f.write(''.join(str(tempAns[j])+'\n'))
        f.write("\n")
        f.write(''.join(str(tempSolution[j])+'\n'))
        f.write("================================================================")
        
    
ary = [1,3,4,11,14,17,22,24,29,31,35,37]
x = 6
s = "LA_SelectionListD.log"
#print(readRes("{:02d}\LA_SelectionList.log".format(x)))
#print(extractRes("LA_SelectionList.log", "LA_SelectionListD.log"))
#buildDict("{:02d}\LA_SelectionListD.log".format(x))
#print(buildDict("{:02d}\{}".format(x,s)))
#print (buildSolution("LA_SelectionListD.log", 0))
extractFinalSolution("LA_SelectionList.log", "LA_SelectionListD.log", "BirdViewVR.txt")
extractFinalSolution("LMA_SelectionList.log", "LMA_SelectionListD.log", "ImmersiveViewVR.txt")




