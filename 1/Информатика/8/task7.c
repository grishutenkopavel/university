#include <stdio.h>
#include <math.h>
int min_instr(int (*arr)[5], int str){
	int j, min = arr[str][0];
	for (j = 1; j < 5; j++)
	{   
		if (min> arr[str][j])
		    min = arr[str][j];
	}
    return min;
}
int main(){
	int i;
	int f[4][5] = { {1, 5, -4, 2,  6},
				  {0, 0, -3, 2, 0},
				  {4, -8, -7, -6, 3},
				  {1, -9, 2, 6, 3} };
	for (i = 0; i < 4; i++)
        printf("%d\n", min_instr(f, i));
    return 0;
}