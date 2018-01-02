# pip install matplotlib
# y = x^2 y=x^3 그래프 그리기

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6), dpi=80)
xs = np.linspace(0.0,10.0,1000)
ys = [x * x for x in xs]
zs = [x * x * x for x in xs]

plt.plot(xs,ys)
plt.plot(xs,zs)
plt.title("A simple graph")
plt.legend(['y=x^2','y=x^3'], loc='upper left')
plt.show()