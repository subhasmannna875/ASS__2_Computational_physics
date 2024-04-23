import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def ode(x, y):
    y1, y2 = y
    dydx = [y2, -(2*y2**3 + y1**2 * y2) * 1/np.cos(x)]
    return dydx

def bc(ya, yb):
    return np.array([ya[0] - 2**(-1/4), yb[0] - ((12**(1/4)/2))])

# Define the range of x values where we want to solve the ODE
x = np.linspace(np.pi/4, np.pi/3, 100)

# Initial guess for the solution
y_guess = np.zeros((2, x.size))

# Solve the boundary value problem
sol = solve_bvp(ode, bc, x, y_guess)

# Plot the solution
plt.plot(sol.x, sol.y[0], label='y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution of y'' = -(2(y')^3 + y^2*y')*sec(x)")
plt.legend()
plt.grid()
plt.show()
