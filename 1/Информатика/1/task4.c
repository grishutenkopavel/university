#define E_ 2.718281828459045235360287471352662498
#include <stdio.h>
#include <math.h>
int main(int argc, char** argv)
{
	float x, z, s, r;
	z = 1.12, s = 2.7, x = 0.12;
	r = (2.71*pow(10, 6)*z*pow(tan(log(s)*x), 2))/(pow(E_, -5*tan(x))+fabs(z*x));
	printf("%g\n", r);
	x = 0.14;
	r = (2.71*pow(10, 6)*z*pow(tan(log(s)*x), 2))/(pow(E_, -5*tan(x))+fabs(z*x));
	printf("%g\n", r);
	z = 1.41, s = 2.9, x = 0.16;
	r = (2.71*pow(10, 6)*z*pow(tan(log(s)*x), 2))/(pow(E_, -5*tan(x))+fabs(z*x));
	printf("%g\n", r);
	return 0;
}
