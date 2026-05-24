import numpy as np
import matplotlib.pyplot as plt

# kalkulus 

# fungsi logaritmik 

x = np.linspace(0.1, 10, 400)
y = np.log(x)

plt.plot(x, y, label='f(x) = log(x)')
plt.title("Logarithmic Function")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()

# fungsi trigonometrik

x = np.linspace(-10, 10, 400)
y = np.sin(x)
y = x * np.sin(x)  # Mengalikan dengan x untuk variasi yang lebih menarik

plt.plot(x, y, label='f(x) = x * sin(x)')
plt.title("Trigonometric Function")
plt.xlabel('x')
plt.ylabel('f(x)')  
plt.legend()
plt.show()
