#include <stdio.h>
int main(int argc, char** argv){
	int q, c1 = 2100, c = 4200, m = 1, l = 2260000, h = 330000;
	float q1 = 408e5, q2 = 15e6,q3 = 30e6;
	q = c1*m*20 + h*m + c*m*100 + l*m;
	q1 = q/q1;
	q2 = q/q2;
	q3 = q/q3;
	printf("масса керосина = %f\n", q1);
	printf("масса дров = %f\n", q2);
	printf("масса спирта = %f\n", q3);
	return 0;
}
