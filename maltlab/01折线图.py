import random

import  matplotlib.pyplot as plt

x = [i for i in range(1, 101)]
y = [random.randint(0, 10) for i in range(1, 101)]
plt.plot(x, y)
plt.show()
print(len(y))
print(len(x))