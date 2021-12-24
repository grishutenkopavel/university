#include <stdio.h>
#include <math.h>
#define k 30
double func(float e, float r, float time)
{
	return (e-e/exp(5*time))/r; // функция
}

int main() {
    float time, n = 1, e = 300, r = 150;


    for (time = 0; time < n; time+=0.001)
    {   
        printf("time = %g, M = %g\n",time, func(e, r, time));
    }

    return 0;
}