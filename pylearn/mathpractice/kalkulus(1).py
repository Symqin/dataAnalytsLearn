# Kalkulus
# jenis jenis fungsi

# fungsi linear

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = 2 * x + 1

plt.plot(x, y, label='f(x) = 2x + 1')
plt.title('Fungsi Linear')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()


#fungsi kuadrat

x = np.linspace(-10, 10, 400)
y = x**2 + 2*x + 1

plt.plot(x, y, label='f(x) = x^2 + 2x + 1')
plt.title('Fungsi Kuadrat')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
