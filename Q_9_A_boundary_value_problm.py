import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def ode(x, y):
    y1, y2 = y
    dydx = [y2, -np.exp(-2*y1)]
    return dydx

def bc(ya, yb):
    return np.array([ya[0] - 0, yb[0] - np.log(2)])

# Initial guess for the solution
x = np.linspace(1, 2, 100)
y_guess = np.zeros((2, x.size))
x_valus=x.copy()
def exact(x):
    return np.log(x)
y_exat=exact(x_valus)

# Solve the boundary value problem
sol = solve_bvp(ode, bc, x, y_guess)

# Plot the solution
plt.plot(sol.x, sol.y[0], label='numarical solution',linestyle="--")
plt.plot(x_valus,y_exat,label='analytical solution')
'''
plt.plot(sol.x,sol.y[1],label="y' ")
'''
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of y\'\' = -e^(-2y)')
plt.legend()
plt.grid()
plt.show()
