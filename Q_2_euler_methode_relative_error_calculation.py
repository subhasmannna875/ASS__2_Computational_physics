import math
import matplotlib.pyplot as plt

def f(t, y):
    return y / t - y**2

def analytical_solution(t):
    return t / (1 + math.log(t))

def euler_method(f, t0, y0, h, t_target):
    t_values = [t0]
    y_values = [y0]
    while t_values[-1] < t_target:
        t_new = t_values[-1] + h
        y_new = y_values[-1] + h * f(t_values[-1], y_values[-1])
        t_values.append(t_new)
        y_values.append(y_new)
    return t_values, y_values

t0 = 1
y0 = 1
h = 0.1
t_target = 2

# Using Euler's method to approximate the solution
t_values, y_values = euler_method(f, t0, y0, h, t_target)

# Analytical solution
analytical_y_values = [analytical_solution(t) for t in t_values]

# Computing absolute and relative errors
absolute_errors = [abs(analytical_y - approx_y) for analytical_y, approx_y in zip(analytical_y_values, y_values)]
relative_errors = [abs((analytical_y - approx_y) / analytical_y) for analytical_y, approx_y in zip(analytical_y_values, y_values)]

print("Absolute Errors:", absolute_errors)
print("Relative Errors:", relative_errors)

# Plotting the results
plt.plot(t_values, y_values, label="Approximated Solution using euler methode")
plt.plot(t_values, analytical_y_values, label="Analytical Solution")
plt.plot(t_values,absolute_errors,label=" absolute error  ")
plt.plot(t_values,relative_errors,label="Relative erro")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Approximated vs Analytical Solution using Euler's Method")
plt.legend()
plt.grid()
plt.show()


'''

 out put 
Absolute Errors: [0.0, 0.004281727936202406, 0.02404322312465057, 0.054518923117764295, 0.09233646714443078, 0.13507672988887065,
0.18099835818044185, 0.2288497839352629, 0.27773544349671275, 0.327018895183804, 0.376252229270284]
Relative Errors: [0.0, 0.004263472905159145, 0.02368901749590106, 0.052940569447012475, 0.08814651769015609, 0.1265637538507726,
 0.16629265213298067, 0.2060493791416394, 0.24499146308597577, 0.2825880231101745, 0.3185252005841877]


'''
