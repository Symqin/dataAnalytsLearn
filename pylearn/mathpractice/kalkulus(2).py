import numpy as np
import matplotlib.pyplot as plt

#kalkulus

# fungsi polynomial

x = np.linspace(-10, 10, 400)
y = 0.1 * x**3 - 0.5 * x**2 + 2 * x - 1

plt.plot(x, y, label='f(x) = 0.1x^3 - 0.5x^2 + 2x - 1')
plt.title("Polynomial Function")
plt.legend()
plt.show()

# fungsi eksponensial

x = np.linspace(-10, 10, 400)
y = 2**x
plt.plot(x, y, label='f(x) = 2^x')
plt.title("Exponential Function")
plt.legend()
plt.show()