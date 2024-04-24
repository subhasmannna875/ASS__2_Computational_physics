import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

# Define the function representing the differential equation
def ode(x, y):
    return np.vstack((y[1], y[1]*np.cos(x) - y[0]*np.log(y[0] + 1e-10)))  # Add small positive offset

# Define the boundary conditions
def bc(ya, yb):
    return np.array([ya[0] - 1, yb[0] - np.exp(1)])

# Define the x values for integration
x = np.linspace(0, np.pi/2, 100)
x_valus=x.copy()
# Exact solution  that is given in the book 
def exact(x):
    return np.exp(np.sin(x))
y_exat=exact(x_valus)

# Adjusted initial guess to ensure positivity of y1
y_guess = np.zeros((2, x.size))
y_guess[0] = 1  # Initialize y1 with a positive value

# Solve the boundary value problem
sol = solve_bvp(ode, bc, x, y_guess)

# Plot the solution
plt.plot(sol.x, sol.y[0], label=' numarical Solution',linestyle="--")
plt.plot(x_valus,y_exat,label='exact analytic solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution of y'' = y'cos(x) - yln(y)")
plt.grid(True)
plt.legend()
plt.show()
