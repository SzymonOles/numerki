import numpy as np
import matplotlib.pyplot as plt


def p(x):
    return (x**5) - (x**4 * 137 / 60) + (x**3 * 15 / 8) - (x**2 * 17 / 24) + (9 * x / 8) - (1/120)


def q(x):
    return (x*(x*(x*((x - (137/60))*x + (15/8)) - (17/24))+(9/8))-(1/120))


x00 = np.float32(2/3)
x01 = np.float64(2/3)
y00 = np.float32(2/3)
y01 = np.float64(2/3)
z0 = []
z1 = []

ran = 1000
print("\n\nf32:\n")
for i in range(ran):
    x00 = p(x00)
    y00 = q(y00)
    # print(x00, "\t", y00)
    print(abs(x00-y00))
    z0.append(abs(x00-y00))

print("\n\nf64: \n")
for i in range(ran):
    x01 = p(x01)
    y01 = q(y01)
    # print(x01, "\t", y01)
    print(abs(x01-y01))
    z1.append(abs(x01-y01))

xax = np.arange(0,ran,1)

plt.plot(xax , z0 , label="f32")
plt.plot(xax , z1 , label="f64")
plt.legend()
plt.show()