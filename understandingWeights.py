import matplotlib.pylab as plt
import numpy as np

# Using the same input we used on the Sigmoid Function.
x = np.arange(-8, 8, 0.1);

'''
Weights (w) are the variables that are changed during the learning process, and,
along with the input (probably doesn't change), determine the output of the node.
'''
w1 = 0.5;
w2 = 1.0;
w3 = 2.0;
l1 = 'w = 0.5';
l2 = 'w = 1.0';
l3 = 'w = 2.0';

# For each weight and label.
for w, l in [(w1, l1), (w2, l2), (w3, l3)]:
    # The activation function will use the x multiplied by the different weights.
    f = 1 / (1 + np.exp(-x*w));
    plt.plot(x, f, label=l);

plt.xlabel('x');
plt.ylabel('h_w(x)');
plt.legend(loc=2);
plt.show();