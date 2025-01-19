print('hellow')


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(1000)

plt.hist(x,100)
plt.title("Normal Distribution With Matplotlib")
plt.savefig("Matplotlib_first.png")
plt.show()