def f(x,u):
    return  1/((1-u)**2*x**2+u**2)
def runge_kutta(f, x0, u0, h, u_target):
    x_values = [x0]
    u_values = [u0]
    while u_values[-1] < u_target:
        k1 = h * f(x_values[-1], u_values[-1])
        k2 = h * f(x_values[-1] + 0.5 * k1, u_values[-1] + 0.5 * h)
        k3 = h * f(x_values[-1] + 0.5 * k2, u_values[-1] + 0.5 * h)
        k4 = h * f(x_values[-1] + k3, u_values[-1] + h)
        
        x_new = x_values[-1] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        u_new = u_values[-1] + h
        
        x_values.append(x_new)
        u_values.append(u_new)
    return x_values, u_values

# Initial values
x0 = 1
u0 = 0
h = 0.0001  # Step size
u_target =1

# Solve using Runge-Kutta method
x_values, u_values = runge_kutta(f, x0, u0, h, u_target)

#finding  value of x at a perticuler given point
t=3.5*(10)**6
desired_u =t/(1+t)
import numpy as np

def linear_interpolation(x_values, u_values, u_target):
    # Find the index of the last element in u_values that is less than u_target
    idx = np.where(np.array(u_values) < u_target)[0][-1]
    # Perform linear interpolation between the two nearest points
    x_interpolated = x_values[idx] + (x_values[idx + 1] - x_values[idx]) * (u_target - u_values[idx]) / (u_values[idx + 1] - u_values[idx])

    return x_interpolated



# Interpolate the solution at a specific value of u=t/(1+t)

x_interpolated = linear_interpolation(x_values, u_values, desired_u)
print("Interpolated value of x at t=3.5*10^6 ( u=", desired_u, "):", x_interpolated)

import matplotlib.pyplot as plt
plt.scatter(desired_u,x_interpolated,color="red")
plt.plot(u_values,x_values)
plt.xlabel("u")
plt.ylabel("value of x")
plt.title("u Vs x (u=t/(1+t))")
plt.grid()
plt.show()

'''
Interpolated value of x at t=3.5*10^6 ( u= 0.9999997142857959 ): 2.144818469572913
'''