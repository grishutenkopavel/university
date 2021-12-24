#include <stdio.h>
#define _i 10
int sum_arr(int *arr, int size) {
	int sum;
		if(size == -1) {
			sum = 0;
			return sum;
	}
	printf("%d ", arr[size]);
	sum = sum_arr(arr, size - 1) + arr[size];
	return sum;
}
int main(){
	
	int n[_i] = {-1, 2, 3, -4, 5, 6, -7, 8, 9, -1};
	printf("\n%d", sum_arr(n, _i-1));
    return 0;
}