import csv
Ans = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
Seq = ['A', 'E', 'B', 'C', 'D', 'F', 'G', 'I', 'J', 'K', 'H', 'L', 'M', 'N']

filePath = 'E:\\Other\\PythonScript\\MasterThesisRes\\ParticipantsData.csv'
'''
f = open(filePath,'r')
for x in f:
    print(x)
'''
with open(filePath) as csv_file:
    List = []
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for x in csv_reader:
        for y in x[2]:
            if(y >= 'A' and y <= 'Z'):
                List.append(y)
    print(List)
    Seq = List    


lenS = len(Ans)
DP = [[0.0 for i in range(lenS)] for i in range(lenS)]

def compareStr():
    for i in range(lenS):
        DP[i][0] = i
    for i in range(lenS):
        DP[0][i] = i
    for i in range(lenS):
        for j in range(lenS):
            DP[i][j] = min(DP[i-1][j-1]+int(Ans[i] != Seq[j]), DP[i-1][j]+0.5, DP[i][j-1]+0.5)
    print(DP[lenS-1][lenS-1])

compareStr()


