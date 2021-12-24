#include <stdio.h>
int main(int argc, char** argv){
	int x = 17, p;
	p = (((2*x - 3)*x + 2)*x + 1)*x + 3;
	printf("p = %d", p);
	return 0;
}
