import numpy as np
import matplotlib.pyplot as plt

btc = np.genfromtxt("btc.data",delimiter='\t',dtype=str)
eth = np.genfromtxt("eth.data",delimiter='\t',dtype=str)
sindat = np.arange(57 , 129 , 0.1)

btc1 =[]
btc2 =[]
for x in range(len(btc)):
    btc1.append(float(btc[x][0]))
    btc2.append(float(btc[x][1]))

eth1 =[]
eth2 =[]
for x in range(len(eth)):
    eth1.append(float(eth[x][0]))
    eth2.append(float(eth[x][1]))

plt.subplot(311)
plt.plot(btc1,btc2)
plt.xlim((57,129))
# plt.xticks(())
plt.ylabel("btc")

plt.subplot(312)
plt.plot(eth1,eth2)
plt.xlim((57,129))
# plt.xticks(())
plt.ylabel("eth")

plt.subplot(313)
plt.plot(sindat,np.sin(sindat))
plt.xlim((57,129))
plt.xlabel("dni od 01.01.2021")
plt.ylabel("sin")

plt.show()
