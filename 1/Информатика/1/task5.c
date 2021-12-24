#include <stdio.h>
#include <math.h>
int main(int argc, char** argv)
{
	float x, y;
	scanf("%g%g", &x, &y);
	y = -2*sqrt(y*y+4*x*x/3)-pow(cos(x), 4)/x;
	printf("%g\n", y);
	return 0;
}
