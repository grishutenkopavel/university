#include <stdio.h>
#include <math.h>
int main(int argc, char** argv)
{
	float x, y, u;
	scanf("%g%g", &x, &y);
	u = sin(x + y);
	u = (1 + pow(u, 2))/(2 + fabs(x - 2*x*x/(1+fabs(u))));
	printf("%g\n", u);
	return 0;
}
