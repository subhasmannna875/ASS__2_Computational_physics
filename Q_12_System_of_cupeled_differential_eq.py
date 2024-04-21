import numpy as np
import matplotlib.pyplot as plt

def f(t, u):
    u1, u2, u3 = u  # u is a vector have three element
    du1dt = u1 + 2*u2 - 2*u3 + np.exp(-t)
    du2dt = u2 + u3 - 2*np.exp(-t)
    du3dt = u1 + 2*u2 + np.exp(-t)
    return [du1dt, du2dt, du3dt]

def runge_kutta(f, u0, t0, h, t_target):
    t_values = [t0]
    u_values = [u0]
    while t_values[-1] < t_target:
        k1 = np.array(f(t_values[-1], u_values[-1]))
        k2 = np.array(f(t_values[-1] + 0.5 * h, u_values[-1] + 0.5 * h * k1))
        k3 = np.array(f(t_values[-1] + 0.5 * h, u_values[-1] + 0.5 * h * k2))
        k4 = np.array(f(t_values[-1] + h, u_values[-1] + h * k3))
        
        u_new = u_values[-1] + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        t_new = t_values[-1] + h
        
        t_values.append(t_new)
        u_values.append(u_new)
    return t_values, u_values

# Initial values
u0 = [3, -1, 1]
t0 = 0
h = 0.01  # Step size
t_target = 1

# Solve using Runge-Kutta method
t_values, u_values = runge_kutta(f, u0, t0, h, t_target)
u1=[u[0] for u in u_values]
u2=[u[1] for u in u_values]
u3=[u[2] for u in u_values]

# Plot the results
plt.plot(t_values, u1,color="blue",label="u1")
plt.plot(t_values,u2,color="red",label="u2")
plt.plot(t_values,u3,color="green",label="u3")
plt.legend()
plt.xlabel('t')
plt.ylabel('u')
plt.title('Solution of the System of Differential Equations')


plt.grid(True)
plt.show()
