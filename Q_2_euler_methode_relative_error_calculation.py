import numpy as np
import matplotlib.pyplot as plt

def euler(f,t0,y0,tf,h):
    result=[(t0,y0)]
    t=t0
    y=y0
    n=int((tf-t0)/h)
    for i in range(1,n+1):
        y+=h*f(y,t)
        t+=h
        result.append((t,y))
    return result

def f(y,t):
    return (y/t)-(y/t)**2
t0=1
tf=2
y0=1
h=0.1

solution=euler(f,t0,y0,tf,h)

y_values=[t[1] for t in solution]
t_values=[t[0] for t in solution]

plt.plot(t_values,y_values,label="solution by euler method")

def original_soln(t):
    return t/(1+np.log(t))

orig_soln=original_soln(t_values)

absolute_error=np.abs(y_values-orig_soln)
relative_error=np.abs((y_values-orig_soln)/y_values)

tt=np.linspace(1,2,1000)
plt.plot(tt,original_soln(tt),label="Original solution")
plt.grid()
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()


print("t\t\t euler soln\t\t original soln \t\t abs error\t\t relative error ")
for t, euler_soln,orig_soln,abs_error,rel_error in zip(t_values,y_values,orig_soln,absolute_error,relative_error):
    print(f"{t:.1f}\t\t {euler_soln:.6f}\t\t{orig_soln:.6f}\t\t {abs_error:.6f}\t\t {rel_error:.6f}")


plt.show()

'''
out put
t                euler soln              original soln           abs error               relative error 
1.0              1.000000               1.000000                 0.000000                0.000000
1.1              1.000000               1.004282                 0.004282                0.004282
1.2              1.008264               1.014952                 0.006688                0.006633
1.3              1.021689               1.029814                 0.008124                0.007952
1.4              1.038515               1.047534                 0.009019                0.008685
1.5              1.057668               1.067262                 0.009594                0.009071
1.6              1.078461               1.088433                 0.009972                0.009246
1.7              1.100432               1.110655                 0.010223                0.009290
1.8              1.123262               1.133654                 0.010392                0.009251
1.9              1.146724               1.157228                 0.010505                0.009161
2.0              1.170652               1.181232                 0.010581                0.009038



'''