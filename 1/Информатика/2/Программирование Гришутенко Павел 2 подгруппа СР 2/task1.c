#include <stdio.h>
#include <math.h>
int main(int argc, char** argv){
	float v0 = 200., a = 58., g = 10., h = 80., s;
	a=a*180/M_PI;
	s = (v0*v0*sin(a)*cos(a)+v0*cos(a)*sqrt(pow(v0*sin(a), 2)+2*g*h))/g;
	printf("S = %f", s);
	return 0;
}
