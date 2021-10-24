import numpy as np
import matplotlib.pyplot as plt

x00 = np.float16(1/3)
x01 = np.float32(1/3)
x02 = np.float64(1/3)
z0 = []
z1 = []
z2 = []

zasieg = 35


def funkcja(z, zbior):
    for i in range(zasieg):
        z = 4*z - 1
        zbior.append(z)


osx = np.arange(0, zasieg, 1)

funkcja(x00, z0)
funkcja(x01, z1)
funkcja(x02, z2)

plt.subplot(311)
plt.plot(osx, z0)
plt.ticklabel_format(useOffset=False)
plt.ylabel("float16")
plt.subplot(312)
plt.plot(osx, z1)
plt.ticklabel_format(useOffset=False)
plt.ylabel("float32")
plt.subplot(313)
plt.plot(osx, z2)
plt.ticklabel_format(useOffset=False)
plt.ylabel("float64")
plt.show()

plt.plot(osx, z0 , label= "float16")
plt.plot(osx, z1, label= "float32")
plt.plot(osx, z2, label= "float64")
plt.ticklabel_format(useOffset=False)
plt.legend()
plt.show()

