import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def ode(x, y):
    y1, y2 = y
    dydx = [y2, 1/2 - (y2**2)/2 - y1 * np.sin(x)/2]
    return dydx

def bc(ya, yb):
    return np.array([ya[0] - 2, yb[0] - 2])

# Define the range of x values where we want to solve the ODE
x = np.linspace(0, np.pi, 100)
x_valus=x.copy()
# Exact solution  that is given in the book 
def exact(x):
    return 2+np.sin(x)
y_exat=exact(x_valus)

# Initial guess for the solution
y_guess = np.zeros((2, x.size))

# Solve the boundary value problem
sol = solve_bvp(ode, bc, x, y_guess)

# Plot the solution
plt.plot(sol.x, sol.y[0], label='numarical solution',linestyle="--")
plt.plot(x_valus,y_exat,label="exact analytical solution")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution of y'' = 1/2 - (y')^2/2 - y*sin(x)/2")
plt.legend()
plt.grid()
plt.show()
