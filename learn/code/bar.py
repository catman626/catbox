import matplotlib.pyplot as plt
import numpy as np


plt.subplot([2, 1, 1])

a = np.array([1, 2, 3, 6])
b = np.array([5, 6, 7, 8])

plt.bar(a, b)

plt.show()
