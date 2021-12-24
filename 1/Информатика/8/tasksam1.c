#include <stdio.h>
#include <math.h>
void copy_mtr(float (*oarr)[2], float(*iarr)[2]) {
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			iarr[i][j] = oarr[i][j];
		}
	}
}
int fact(int k) {
	if (k == 1)
		return 1;
	return fact(k - 1) * k;
}
void pow_arr(float(*parr)[2], float (*arr)[2], int k) {
	float tarr1[2][2];
	float tarr2[2][2];
	copy_mtr(arr, tarr1);
	for (int n = 1; n < k; n++) {
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 2; j++) {
				tarr2[i][j] = tarr1[i][0] * arr[0][j] + tarr1[i][1] * arr[1][j];
			}
		}
		copy_mtr(tarr2, tarr1);
	}
	copy_mtr(tarr2, parr);
}
void matrsin(float(*arr)[2]) {
	float msin[2][2];
	float parr[2][2];
	double fm, r;
	int n = 2, k, p;
	copy_mtr(arr, msin);
	do {
		p = n + 1;
		k = 2 * n - 1;
		fm = pow(-1, p) / fact(k);
		pow_arr(parr, arr, k);
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 2; j++) {
				msin[i][j] += fm * parr[i][j];
			}
		}	
		n++;
	} while (n != 7);
	copy_mtr(msin, arr);
}
int main(){
	float a[2][2] = { {1, 2}, {3, 4} };
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++)
			printf("%g ", a[i][j]);
		printf("\n");
	}
	matrsin(a);
	printf("\n");
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++)
			printf("%g ", a[i][j]);
		printf("\n");
	}
    return 0;
}