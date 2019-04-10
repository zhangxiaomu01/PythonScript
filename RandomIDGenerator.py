import random
dic = ['VR', 'VE']
def getRandom():
    ind = random.randrange(0,2)
    res = ""
    res = res + dic[ind]
    num = random.randrange(1000, 10000)
    res = res + str(num)
    print(res)

i = 1
while(i==1):
    getRandom()
    i = int(input())

