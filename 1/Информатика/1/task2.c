#include <stdio.h>
int main(int argc, char** argv)
{
	int a, sum = 0;
	scanf("%d",&a);
	while (a)
	{
		sum = sum + a % 10;
		a = a / 10;
	}
	printf("%i\n", sum);
	return 0;
}
