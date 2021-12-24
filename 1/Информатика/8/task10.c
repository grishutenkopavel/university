#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define _H  6.626e-34
#define _Me  9.1e-31
#define _C  2.998e8
#define _Lm  2.5e-7

float func1(float a)
{
	float hv = (float)(_H * _C) / _Lm; // vi = c/lm
	if (hv < a)
		return 0;
	else {
		float v = sqrt((2 / _Me) * (hv - a));
		return v;
	}
}

int main()
{
	float a;
	printf("Enter the number A: ");
	scanf("%f", &a);
	a *= 1.602e-19;
	printf("V = %g\n", func1(a));
	return 0;
}
