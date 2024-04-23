import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the function f(t, y)
def f(t, y):
    return 1 + y / t

# Define the time span
t_span = (1, 2)

# Define the initial condition
y0 = [2]

# Solve the initial value problem
sol = solve_ivp(f, t_span, y0, t_eval=np.linspace(1, 2, 100))

def exact(t):
    return 2*t+t*np.log(t)
t_eval=np.linspace(1, 2, 100)
y_exact=exact(t_eval)
# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], label='numarical Solution',linestyle="--")
plt.plot(t_eval,y_exact,label="analytic solution get from mathematica")
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solution of y\' = 1 + y/t with y(1) = 2')
plt.grid()
plt.legend()
plt.show()
