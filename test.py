
import time
from datetime import datetime
from dateutil import parser
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=1)

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 2]
neigh.fit(X, y)
print(neigh.predict([[3.3]]))
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()
# t = '04:13:13.336280'
# parsed = t.split(':')
# result = int(parsed[0])*3600+int(parsed[1])*60+float(parsed[2])
# print(result)
### Use this space to try out ideas and free code ###

# print(int(3.9))