
import sys
import math

def distance(x1, y1, x2, y2):
        res = math.sqrt((y2 - y1)*(y2-y1) + (x2 - x1) * (x2-x1))
        return res


(a, F) = (int(input()), [x.strip().split(" ") for x in sys.stdin.readlines()])
X=[0]*a
Y=[0]*a
G=[0]*a


for j in range (0,a):
        X[j]=int(F[j][0])
        Y[j]=int(F[j][1])
        G[j]=int (F[j][2])

opt = [0]*a

opt[0] = G[0]

for i in range(1, a):
    opt[i] = opt[0] + G[i] - distance(X[0], Y[0], X[i], Y[i])
    for k in range(1, i):
        if opt[i] < opt[k] + G[i] - distance(X[k], Y[k], X[i], Y[i]):

            opt[i] = opt[k] + G[i] - distance(X[k], Y[k], X[i], Y[i])

answer= (round(opt[a - 1], 6))
print(answer)

