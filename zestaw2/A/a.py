import numpy as np

choice = 3
ran = 15

#pythonowe auto floaty
if choice == 1:
    f = 3.0
    for i in range(ran):
        print (i, f)
        f = f ** 2

#przykladowa obsluga overflow dla auto floatow
if choice == 2:
    try:
        f = 3.0
        for i in range(ran):
            print (i, f)
            f = f ** 2
    except OverflowError as err:
        print ('error: ', f, err)

#numpy float32
if choice == 3:
    x = np.float32(3.0)
    for i in range(ran):
        print (i, x)
        x = x ** 2

#numpy float64
if choice == 4:
    y = np.float64(3.0)
    for i in range(ran):
        print (i, y)
        y = y ** 2

#przykladowa obsluga overflow dla numpy float32
np.seterr(over='raise')
if choice == 5:
    try:
        x = np.float32(3.0)
        for i in range(ran):
            print (i, x)
            x = x ** 2
    except:
        print ('overflow')

#przykladowa obsluga overflow dla numpy float64
if choice == 6:
    try:
        y = np.float64(3.0)
        for i in range(ran):
            print (i, y)
            y = y ** 2
    except:
        print ('overflow')