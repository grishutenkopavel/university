#include <stdio.h>
int c(int m, int n) {
	if (m  == 0)
		return 1;
	if (m == n)
		return 1;
	return c(m, n-1)+c(m-1, n-1);
}
int main(){
	int m, n;
	scanf("%d%d", &m, &n);
	printf("%d", c(m, n));
    return 0;
}