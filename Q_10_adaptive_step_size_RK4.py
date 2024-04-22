import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return (y**2 + y) / t

def rk4_step(f, t, y, h):
    k1 = h * f(t, y)
    k2 = h * f(t + h/2, y + k1/2)
    k3 = h * f(t + h/2, y + k2/2)
    k4 = h * f(t + h, y + k3)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6

def rk4_adaptive(f, t0, y0, tf, h0, tol):
    t_values = [t0]
    y_values = [y0]
    h = h0
    t = t0
    


    while t < tf:
        error=0
        while error <tol:
            y1 = rk4_step(f, t, y_values[-1], 2*h)#  euler uith 2h step
            y2_half = rk4_step(f, t, y_values[-1], h) # euler with h step
            y2 = rk4_step(f, t+h, y2_half, h)
            error = np.abs(y2 - y1)
            
            rho=(30*h*tol)/(error)
            h =h*(rho)**(1/4)
        t +=2*h
        t_values.append(t)
        y_values.append(y2)
        
    
    return np.array(t_values), np.array(y_values)


# Initial conditions
t0 = 1
y0 = -2
tf = 3

# Adaptive step-size parameters
h0 = 0.01
tol = 1e-4  #  we can chenge tol according to our accuracy

# Solve the ODE using adaptive RK4
t_values, y_values = rk4_adaptive(f, t0, y0, tf, h0, tol)

# Plot the solution
plt.figure(figsize=(10, 6))
plt.plot(t_values, y_values, label='Solution')
plt.scatter(t_values, y_values, color='red', label='Mesh Points')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solution of y\' = (y^2 + y) / t with Adaptive RK4')
plt.legend()
plt.grid(True)
plt.show()
