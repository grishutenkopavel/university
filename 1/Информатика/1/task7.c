#include <stdio.h>
#include <math.h>
int main(int argc, char** argv)
{
	float a, b, c, x, h;
	a = 0.12, b = 3.5, c = 2.4, x = 1.4;
	h = -(x - a)/pow(x*x+a*a, 1/3) - 4*pow(x*x+b*b,0.75)/(2+a+b+pow(x-c, 2/3));
	printf("%g\n", h);
	x = 1.6;
	h = -(x - a)/pow(x*x+a*a, 1/3) - 4*pow(x*x+b*b,0.75)/(2+a+b+pow(x-c, 2/3));
	printf("%g\n", h);
	a = 0.27, b = 3.9, c = 2.8, x = 1.8;
	h = -(x - a)/pow(x*x+a*a, 1/3) - 4*pow(x*x+b*b,0.75)/(2+a+b+pow(x-c, 2/3));
	printf("%g\n", h);
	return 0;
}
