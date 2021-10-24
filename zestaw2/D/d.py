import numpy as np
import matplotlib.pyplot as plt

x0 = np.float32(2/3)
x0eps = np.finfo(x0).eps

x1 = np.float64(2/3)
x1eps = np.finfo(x1).eps

z1 = []
z2 = []


def alpha(n, eps):
    return n * 4 * eps


a = 1
b = -4


def c(i, eps):
    return 4 + alpha(i, eps)


for i in range(-256, 0):
    x = (-b + np.sqrt(b*b - 4 * a * c(i, x0eps))/2)
    z1.append(x)

for i in range(-256, 0):
    x = (-b + np.sqrt(b*b - 4 * a * c(i, x1eps))/2)
    z2.append(x)

# print(z1,"\n\n\n",z2)

xos = np.arange(-256, 0, 1)

plt.plot(xos, z1, label="float32")
plt.plot(xos, z2, label="float64")
plt.ticklabel_format(useOffset=False)
plt.legend()
plt.show()

plt.subplot(211)
plt.plot(xos, z1, label="float32")
plt.legend()
plt.ticklabel_format(useOffset=False)
plt.subplot(212)
plt.plot(xos, z2, label="float64")
plt.legend()
plt.ticklabel_format(useOffset=False)
plt.show()