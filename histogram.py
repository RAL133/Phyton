#
# Template for Python program
# Name: Russel Aristo
#

import matplotlib.pyplot as plt
import numpy as np
 
# 1. Input
x = np.random.normal(90,1,100)
#(mean,standart deviation, data point)


# 2. Process

# 3. Output
plt.title("Histogram: Russel Aristo")
plt.xlabel("Distribution")
plt.ylabel("Score")
plt.xlim([0,100])
plt.hist(x)
plt.show()