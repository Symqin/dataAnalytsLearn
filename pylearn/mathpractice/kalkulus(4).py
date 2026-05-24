# kalkulus 
import numpy as np
import matplotlib.pyplot as plt


# Derivatif (turunan)

def f(x):return 3 * x**3 - 6 * x**2 + x - 4

def first_derivative(x): return 9 * x**2 - 12 * x + 1

def second_derivative(x): return 18 * x - 12

x = np.linspace(-2, 3, 400)

plt.plot(x, f(x), label='f(x) (biaya asli)')
plt.plot(x, first_derivative(x), label="f'(x) (turunan pertama)")
plt.plot(x, second_derivative(x), label="f''(x) (turunan kedua)"    )

plt.title("Derivatif of polynomial function")
plt.legend()
plt.grid(True)
plt.show()


# gradient descent

def f(x): return x**2 - 4*x + 3

def df_dx(x): return 2*x - 4

def gradient_descent(init_x, learning_rate=0.1, iterations=10):
    x = init_x
    x_history = [x]
    for _ in range(iterations):
        grad = df_dx(x)
        x -= learning_rate * grad
        x_history.append(x)
    return x, x_history

x_min, x_history = gradient_descent(0.0)
x = np.linspace(-2, 4, 400)
y = f(x)

plt.plot(x, y, 'r-', label='f(x) = x^2 - 4x + 3')
plt.plot(x_history, f(np.array(x_history)), 'bo', label='Gradient Descent', markersize=3)
plt.title("Gradient Descent Visualization")
plt.legend()
plt.show()

# integral

def f(x): return x

def F(x): return x**2 / 2

x = np.linspace(0, 2, 400)
y = f(x)
F_y = F(x)

fig, ax = plt.subplots()
ax.plot(x,y, 'r', linewidth=2, label='f(x) = x')
ax.plot(x, F_y, 'g', linewidth=2, label='F(x) = x^2 / 2')

ax.fill_between(x,y, where=[(xi > 0) and (xi < 1) for xi in x], color='skyblue', alpha=0.5,)

ax.set_title("Integral Visualization")
ax.legend()
ax.grid(True)
plt.show()

