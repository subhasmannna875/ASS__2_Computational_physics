import numpy as np
import matplotlib.pyplot as plt

# Define constants
g = 10
t1 = 10
num_points = 100
t = np.linspace(0, t1, num_points)
tolerance = 1e-3
max_iter = 10000
h = t1 / (num_points - 1)
x = np.zeros(num_points)

# Relaxation parameter
w = 1.92
all_solution = []

# Calculation using relaxation method
for i in range(max_iter):
    x_last = x.copy()
    for j in range(1, num_points - 1):
        x[j] = (1 - w) * x[j] + w * (0.5 * (x[j+1] + x[j-1]) + 0.5 * g * h**2)
    all_solution.append(x.copy())
    if max(abs(x - x_last)) < tolerance:
        print(f"Solution converged after {i+1} steps.")
        break

# Exact solution
def exact(t):
    return (5 * 10 * t - (10 * t**2) / 2)

t_values = t.copy()
x_exact = exact(t)

# Plotting
plt.figure(figsize=(10, 6))


plt.plot(t_values, all_solution[-1],color="red" ,label='numarical Solution')
plt.plot(t_values, all_solution[95],label="itaration no 96 ")
plt.plot(t_values, all_solution[110],label="itaration no 111 ")
plt.plot(t_values, all_solution[80],label="itaration no 81 ")
plt.plot(t_values, all_solution[65],label="itaration no 66 ")
plt.plot(t_values, all_solution[55],label="itaration no 56 ")
plt.plot(t_values, x_exact, label='Exact Solution', linestyle=':', color='black')
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Relaxation Method Convergence')
plt.legend()
plt.grid(True)
plt.show()
