#include <stdio.h>
#include <math.h>
#define k 0.0168 // k = -ln(v1/v0)
double func(double v0, int distance)
{
	return v0*exp(-k*distance); // функция
}

int main() {
    int distance,  r = 150, s = 1; 
    double v0 = 12, v1 = 11.8;
    
    for (distance = 0; distance < r; distance++)
    {   
        printf("range = %i, V = %g\n",distance, func(v0, distance));
    }
    
    return 0;
}
