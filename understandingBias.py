import matplotlib.pylab as plt
import numpy as np

# Using the same input we used on the Sigmoid Function.
x = np.arange(-8, 8, 0.1);

w = 5.0;
b1 = -8.0;
b2 = 0.0;
b3 = 8.0;
l1 = 'b = -8.0';
l2 = 'b = 0.0';
l3 = 'b = 8.0';

for b, l in [(b1, l1), (b2, l2), (b3, l3)]:
    print(x*w+b);
    f = 1 / (1 + np.exp(-(x*w+b)));
    plt.plot(x, f, label=l);

plt.xlabel('x');
plt.ylabel('h_w(x)');
plt.legend(loc=2);
plt.show();