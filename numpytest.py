import numpy as np

print('my numpy version: ', np.__version__)

n = np.random.randint(1,20)
randomlist = []
for i in range (1000000):
    n = n = np.random.randint(1,20)
    randomlist.append(n)
# 
print("randomlist:", randomlist)