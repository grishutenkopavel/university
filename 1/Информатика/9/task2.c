#include <stdio.h>
int fib(int n) {
	if (1 == n)
		return 1;
	if (0 == n)
		return 1;
	return fib(n - 1) + fib(n - 2);
}
int main(){
	int n;
	scanf("%d", &n);
	printf("%d", fib(n));
    return 0;
}