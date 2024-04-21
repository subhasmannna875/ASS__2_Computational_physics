#include <stdio.h>
#include <math.h>

// Function to calculate the exact solution
double exact_solution(double t) {
    return pow(t + 1, 2) - 0.5 * exp(t);
}

// Function to implement Euler's method
void euler_method(double h, double y0, double t_end) {
    double t = 0.0;
    double y = y0;

    printf("t\t\tEuler's y\tExact y\t\tError\t\tError upper Bound\n");

    while (t <= t_end) {
        double error_upper_bound = 0.1* (0.5*exp(2) - 2) *( exp(t)-1) ;
        double exact_y = exact_solution(t);
        double error = fabs(exact_y - y);
        
        printf("%.2f\t\t%.5f\t\t%.5f\t\t%.5f\t\t%.5f\n", t, y, exact_y, error, error_upper_bound);

        // Euler's method iteration
        y = y + h * (y - t * t + 1);
        t += h;
    }
}

int main() {
    double h = 0.2; // Step size
    double y0 = 0.5; // Initial value of y
    double t_end = 2.0; // End value of t

    euler_method(h, y0, t_end);

    return 0;
}
/*
OUT PUT

t               Eulers y       Exact y         Error           Error upper Bound
0.00            0.50000         0.50000         0.00000         0.00000
0.20            0.80000         0.82930         0.02930         0.03752
0.40            1.15200         1.21409         0.06209         0.08334
0.60            1.55040         1.64894         0.09854         0.13931
0.80            1.98848         2.12723         0.13875         0.20767
1.00            2.45818         2.64086         0.18268         0.29117
1.20            2.94981         3.17994         0.23013         0.39315
1.40            3.45177         3.73240         0.28063         0.51771
1.60            3.95013         4.28348         0.33336         0.66985
1.80            4.42815         4.81518         0.38702         0.85568
2.00            4.86578         5.30547         0.43969         1.08264 
*/


