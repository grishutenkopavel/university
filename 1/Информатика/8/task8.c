#include <stdio.h>
int simp(int n){
	int i;
	for (i = 2; i < n; i++){
		if (n % i == 0){
			printf("NO");
			return 0;
		}
	}
	printf("YES");
	return 0;
}
int main(){
	int n;
	scanf("%d",&n);
	simp(n);
    return 0;
}