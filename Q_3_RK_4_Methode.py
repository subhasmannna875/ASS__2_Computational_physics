import matplotlib.pyplot as plt
import numpy as np

def f(x, y, z):
    return z

def g(x, y, z):
    return 2 * z - y + x * (np.exp(x) - 1)

def runge_kutta_4th_order(f, g, x0, y0, z0, h, x_target):
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]
    while x_values[-1] < x_target:
        x = x_values[-1]
        y = y_values[-1]
        z = z_values[-1]

        k1y = h * f(x, y, z)
        k1z = h * g(x, y, z)

        k2y = h * f(x + h / 2, y + k1y / 2, z + k1z / 2)
        k2z = h * g(x + h / 2, y + k1y / 2, z + k1z / 2)

        k3y = h * f(x + h / 2, y + k2y / 2, z + k2z / 2)
        k3z = h * g(x + h / 2, y + k2y / 2, z + k2z / 2)

        k4y = h * f(x + h, y + k3y, z + k3z)
        k4z = h * g(x + h, y + k3y, z + k3z)

        y_new = y + (k1y + 2 * k2y + 2 * k3y + k4y) / 6
        z_new = z + (k1z + 2 * k2z + 2 * k3z + k4z) / 6

        x_values.append(x + h)
        y_values.append(y_new)
        z_values.append(z_new)
    return x_values, y_values

# Initial conditions
x0 = 0
y0 = 0
z0 = 0
h = 0.01
x_target = 1

# Using Runge-Kutta 4th order method to approximate the solution
x_values, y_values = runge_kutta_4th_order(f, g, x0, y0, z0, h, x_target)

# Plotting the results
plt.plot(x_values, y_values, label="RK4 Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.title(" solution using 4th-order Runge-Kutta Method ")
plt.legend()
plt.grid()
plt.show()
