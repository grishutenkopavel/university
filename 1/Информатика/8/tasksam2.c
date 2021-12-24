#include <stdio.h>
#define h 0.1

float func(float y) {
	return -0.6 * y;
}
void integ(float *x, float *y) {
	float k1, k2, k3, k4;
	for (int i = 0; i < 100; i++) {
		k1 = func(y[i]);
		k2 = func(y[i] + k1 / 2);
		k3 = func(y[i] + k2 / 2);
		k4 = func(y[i] + k3);
		y[i+1] = y[i]+h/6*(k1 + 2*k2 + 2*k3 + k4);
		x[i+1] = x[i]+h;
	}
}
int main() {
	float x[101];
	float y[101];
	x[0] = 0;
	y[0] = 2;
	integ(x, y);
	for (int i = 0; i < 101; i++)
		printf("x =%g y = %g\n", x[i], y[i]);
	return 0;
}
