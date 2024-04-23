import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def ode(x, y):
    y1, y2 = y  #y1=y  ,y2=y'
    dydx = [y2, y2 * np.cos(x) - y1 * np.log(y1)]  #define derivitive
    return dydx
# define boundary condition
def bc(ya, yb):
    return np.array([ya[0] - 1, yb[0] - np.exp(1)])

# Define the range of x values where we want to solve the ODE
x = np.linspace(0, np.pi/2, 100)

# Initial guess for the solution
y_guess = np.zeros((2, x.size))

# Solve the boundary value problem
sol = solve_bvp(ode, bc, x, y_guess)

# Plot the solution
plt.plot(sol.x, sol.y[0], label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of y\'\' = y\' * cos(x) - y * ln(y)')
plt.legend()
plt.grid()
plt.show()