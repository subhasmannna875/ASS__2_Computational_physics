import numpy as np
import matplotlib.pyplot as plt

def ode(x, t):
    return -10

def integrate(x0, v0, t):
    h = t[1] - t[0]
    x = np.zeros_like(t)
    v = np.zeros_like(t)
    x[0] = x0
    v[0] = v0
    for i in range(1, len(t)):
        k1 = h * v[i-1]
        l1 = h * ode(x[i-1], t[i-1])
        k2 = h * (v[i-1] + 0.5*l1)
        l2 = h * ode(x[i-1] + 0.5*k1, t[i-1] + 0.5*h)
        k3 = h * (v[i-1] + 0.5*l2)
        l3 = h * ode(x[i-1] + 0.5*k2, t[i-1] + 0.5*h)
        k4 = h * (v[i-1] + l3)
        l4 = h * ode(x[i-1] + k3, t[i-1] + h)
        x[i] = x[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        v[i] = v[i-1] + (l1 + 2*l2 + 2*l3 + l4) / 6
        
    return x
f = lambda v: integrate(0, v, t)[-1] - 0
w=1.3 # relaxation parameter
def secant_method(f, x0, x1, tol=1e-2, max_iter=100):
    
    solutions = []
    for i in range(max_iter):
        x2 = x1 -w* f(x1) * (x1 - x0) / (f(x1) - f(x0)) # hare x1 and x2  are velocity
        solutions.append(x2)
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2
    else:
        raise ValueError("Secant method did not converge")
    return x2, solutions


# Define time grid
t1 = 10
t = np.linspace(0, t1, 100)
# Shooting method parameters 
x0 = 1
x1 = 100
x2,guesses=secant_method(f, x0, x1, tol=1e-2, max_iter=100)
print(guesses)
'''
print(x2)
print(x_values)
'''

def shooting_method(guesses):
    solutions = []
    all_solutions = []
    for guess in guesses:
        x = integrate(0, guess, t)
        all_solutions.append(x)
        solutions.append(x[-1])
    idx = np.argmin(np.abs(np.array(solutions) - 0))  #  index of minimum value of error
    return guesses, all_solutions, idx

t_valus=np.linspace(0, t1, 100)
#exact solution
def exact(t):
    return (5*10*t-(10*t**2)/2)

x_exact=[exact(t) for t in t_valus]


# Solve using shooting method
v0_guesses, all_solutions, idx = shooting_method(guesses)
print("index of array of velocity for which error is minimam",(idx))
print("velocity for which error is minimam",guesses[idx])

# Plotting
plt.figure(figsize=(10, 6))
plt.figure(figsize=(10, 6))
for i, solution in enumerate(all_solutions):
    if i == idx:
        plt.plot(t, solution, linestyle="dotted",label=f'Numerical Solution (Initial Velocity: {guesses[idx]})')
    else:
        plt.plot(t, solution, label=f'Guess Initial Velocity: {guesses[i]} ({i+1})')
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Shooting Method Solutions')
plt.plot(t_valus,x_exact,linestyle="--",color="orange",label="exact solution")
plt.axhline(0, color='k', linestyle='--', label='x axis')
plt.legend()
plt.grid(True)
plt.show()



'''
initial velocity after each etaration:
[35.0, 54.500000000000014, 48.650000000000006, 50.405000000000015, 49.87850000000001, 50.036450000000016, 49.98906500000001, 50.00328050000001, 49.99901585000001]
  
initial value of velocity  for which solution matche with actual boundary condition
49.99901585000001
'''


