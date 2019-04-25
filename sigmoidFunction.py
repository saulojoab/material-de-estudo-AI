import matplotlib.pylab as plt
import numpy as np

x = np.arange(-8, 8, 0.1);
f = 1 / (1 + np.exp(-x));

plt.plot(x, f);
plt.xlabel('x');
plt.ylabel('f(x)');
plt.show();

'''
As can be seen in the figure, the function is “activated” (i.e. it moves from 0 to 1)
when the input x is greater than a certain value. The sigmoid function isn’t a step function
however, the edge is “soft”, and the output doesn’t change instantaneously.
'''