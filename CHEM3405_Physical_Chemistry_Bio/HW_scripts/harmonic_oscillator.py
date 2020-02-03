%matplotlib inline
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
a = 0.001
f = lambda x: (a/np.pi)**(1/4)*np.exp(-a*x**2./2)
x = np.linspace(-100,100,1000)
fig = plt.figure(figsize=(10,10))
plt.plot(f(x), 'k')
plt.show()
