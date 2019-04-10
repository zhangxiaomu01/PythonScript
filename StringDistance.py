Ans = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
Seq = ['A', 'E', 'B', 'C', 'D', 'F', 'G', 'I', 'J', 'K', 'H', 'L', 'M', 'N']

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


