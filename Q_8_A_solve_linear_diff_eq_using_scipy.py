import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the function f(t, y)
def f(t, y):
    return t * np.exp(3 * t) - 2 * y

# Define the time span
t_span = (0, 1)

# Define the initial condition
y0 = [0]

# Solve the initial value problem
sol = solve_ivp(f, t_span, y0, t_eval=np.linspace(0, 1, 100))

# Plot the solution

plt.plot(sol.t, sol.y[0], label='Solution')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solution of y\' = te^(3t) - 2y with y(0) = 0')
plt.grid()
plt.legend()
plt.show()
