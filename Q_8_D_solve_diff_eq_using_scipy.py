import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the function f(t, y)
def f(t, y):
    return np.cos(2*t) + np.sin(3*t)

# Define the time span
t_span = (0, 1)

# Define the initial condition
y0 = [1]

# Solve the initial value problem
sol = solve_ivp(f, t_span, y0, t_eval=np.linspace(0, 1, 100))
# anlytic solution that get from mathematica
def ecact(t):
    return (1/6)*(8- 2*np.cos(3*t)+3*np.sin(2*t))

t_eval=np.linspace(0, 1, 100)
y_exact=ecact(t_eval)
# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], label='numarical Solution from scipy',linestyle="--")
plt.plot(t_eval,y_exact,label="analytic solution get from mathematica ")
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solution of y\' = cos(2t) + sin(3t) with y(0) = 1')
plt.grid()
plt.legend()
plt.show()
