import numpy as np
import matplotlib.pyplot as plt

dane = np.arange(-np.pi , np.pi , 0.1)
plt.plot(dane, np.sin(dane))
plt.ylabel("sin")
plt.show()