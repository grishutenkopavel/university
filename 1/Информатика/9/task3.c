#include <stdio.h>
int k(int n) {
	if (n < 10)
		return 1;
	return k(n / 10) + 1;
}
int main(){
	int n;
	scanf("%d", &n);
	printf("%d", k(n));
    return 0;
}