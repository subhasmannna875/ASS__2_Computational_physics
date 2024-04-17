from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1, 11) 
y0 = np.e
def backward_euler(fun, x, y0):

    y_value = np.zeros(len(x))
    y_value[0] = y0
    h = x[1] - x[0]
    x_value = np.zeros(len(x))
    x_value[0] = x[0]

    for i in range(len(x) - 1):
        x_value[i + 1] = x_value[i] + h
        rt = fsolve(lambda y: y_value[i] + fun(y, y_value[i + 1]) * h - y, y_value[i])  #  backward  euler each step root finding
        y_value[i + 1] = rt

    return x_value, y_value
#first differential equation
def f1(y, x):
    return -9 * y
# second differential equation 
def f2(y,x):
    return -20*(y-x)**2 +2*x

x1_value, y1_value = backward_euler(f1, x, y0)#  solution for first differential equation
y0=1/3
x2_value, y2_value = backward_euler(f2,x,y0)
# Print the results
print("Points:",x1_value)
print("Solution_1:",y1_value)
print("solution_2", y2_value)
plt.plot(x1_value, y1_value, label="Solution for dy/dx = -9y")
plt.plot(x2_value, y2_value,label="Solution for dy/dx = -20(y-x)^2 + 2x")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution for dy/dx = -9y & dy/dx = -20(y-x)^2 + 2x using Backward Euler ")
plt.legend()
plt.grid()
plt.show()



'''
out put 

Points: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]
Solution_1: [2.71828183 1.43067465 0.75298666 0.39630877 0.20858356 0.10978082
 0.05777938 0.0304102  0.01600537 0.00842388 0.00443362]
solution_2 [0.33333333 0.22871355 0.17054343 0.13441087 0.11014641 0.09288949
 0.08006779 0.07020914 0.0624173  0.05611869 0.0509308 ]
'''
