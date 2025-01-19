import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.arange(10)
print(data)

#plt.plot(data)
#plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

#plt.show()


ax3.plot(np.random.standard_normal(50).cumsum(), color='black', linestyle='dashed')
ax1.hist(np.random.standard_normal(100), bins=20, color='black', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30)+3 * np.random.standard_normal(30))


plt.show()