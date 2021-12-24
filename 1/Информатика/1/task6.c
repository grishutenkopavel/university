#include <stdio.h>
#include <math.h>
int main(int argc, char** argv)
{
	float a, B, C, x, R;
	a = 1.7, B = 2.1, C = 3.4, x = 1.05;
	R = B*C/12 * floor(6*x*x*pow(1-x/a, 2) + B*B*pow(1-x/sin(a), 2));
	printf("%g\n", R);
	x = 1.25;
	R = B*C/12 * floor(6*x*x*pow(1-x/a, 2) + B*B*pow(1-x/sin(a), 2));
	printf("%g\n", R);
	a = 1.9, B = 2.5, C = 3.9, x = 1.75;
	R = B*C/12 * floor(6*x*x*pow(1-x/a, 2) + B*B*pow(1-x/sin(a), 2));
	printf("%g\n", R);
	return 0;
}
