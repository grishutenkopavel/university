#include <stdio.h>
#include <math.h>
#define k 0.00044
double func(double m0, int time)
{
	return m0*exp(-k*time); // функция
}

int main() {
    int time, n = 1577; 
    double m0 = 1;

    for (time = 0; time < n; time++)
    {   
        printf("time = %i, T = %g\n",time, func(m0, time));
    }
    return 0;
}