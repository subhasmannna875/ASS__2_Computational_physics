import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the function f(t, y)
def f(t, y):
    return 1 - (t - y)**2

# Define the time span
t_span = (2, 3)
def exact(t):
    return (1-3*t+t**2)/(-3+t)


# Define the initial condition
y0 = [1]

# Solve the initial value problem
sol = solve_ivp(f, t_span, y0, t_eval=np.linspace(2, 3, 100))
t_eval=np.linspace(2, 3, 100)
y_exact=exact(t_eval)
# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], label='Solution',linestyle='--')
plt.plot(t_eval,y_exact,label="exact solution get from mathematica")
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solution of y\' = 1 - (t - y)^2 with y(2) = 1')
plt.grid()
plt.legend()
plt.show()
