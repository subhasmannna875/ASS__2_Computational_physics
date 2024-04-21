import numpy as np
import matplotlib.pyplot as plt

def f(t, y, yp):
    return (t**3 * np.log(t) + 2 * t * yp - 2 * y) / t**2

def euler_method(f, a, b, h, y0, yp0):
    n = int((b - a) / h) + 1
    t_values = np.linspace(a, b, n)
    y_values = np.zeros(n)
    yp_values = np.zeros(n)
    y_values[0] = y0
    yp_values[0] = yp0

    for i in range(1, n):
        yp_values[i] = yp_values[i-1] + h * f(t_values[i-1], y_values[i-1], yp_values[i-1])
        y_values[i] = y_values[i-1] + h * yp_values[i-1]

    return t_values, y_values

def exact_solution(t):
    return (7 * t) / 4 + ((t**3)/2) * np.log(t) - (3/4) * t**3

# Given initial conditions and parameters
a = 1
b = 2
h = 0.001
y0 = 1
yp0 = 0

# Using Euler's method to approximate the solution
t_values, y_values = euler_method(f, a, b, h, y0, yp0)

# Calculating exact solution
exact_values = exact_solution(t_values)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_values, label="Euler's Method Approximation", color='blue')
plt.plot(t_values, exact_values, label="Exact Solution", linestyle='--', color='red')
plt.title("Approximation using Euler's Method vs Exact Solution")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)
plt.show()
