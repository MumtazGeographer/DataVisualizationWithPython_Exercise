import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fig, axes = plt.subplots(2,2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.standard_normal(500), bins=50, color='black', alpha=0.5)
fig.subplots_adjust(wspace=0, hspace=0)
plt.show()