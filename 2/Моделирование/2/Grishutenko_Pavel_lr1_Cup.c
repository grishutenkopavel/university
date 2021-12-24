#include <stdio.h>
#include <math.h>
#define r 0.0373
double func(double t, double ts, int time)
{
	return ts-(ts-t)*exp(-r*time); // функция
}

int main() {
    int time, n = 20; 
    double t = 83, ts = 22;

    for (time = 0; time < n; time++)
    {   
        printf("time = %i, T = %g\n",time, func(t, ts, time));
    }
    printf("%g\n", ts);
    return 0;
}