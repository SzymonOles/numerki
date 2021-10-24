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

ran = 1000
print("\n\nf32  v  64:\n")
for i in range(ran):
    x01 = p(x01)
    y00 = q(y00)
    # print(x00, "\t", y00)
    print(abs(x01-y00))
    z0.append(abs(x01-y00))


xax = np.arange(0,ran,1)

plt.plot(xax , z0 , label="abs f32 vs f64")
plt.legend()
plt.show()