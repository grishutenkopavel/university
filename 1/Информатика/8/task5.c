#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int sum(int** parr, int i){
	int s =0;
	for(int j=0; j <5; j++)
		if(parr[i][j]>0)
			s += parr[i][j];
	return s;
}
int main(int argc, char** argv){
	int i, min = 51, gl;
	int** arr = (int**)malloc(6*sizeof(int*));
	for(i=0; i<6; i++)
		arr[i] = (int*)malloc(5*sizeof(int));
	srand(time(NULL));
	for(int i=0; i<6; i++){
		for(int j=0; j<5; j++){
			arr[i][j] = rand()%10;
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
	for(i=0; i<6; i++){
		gl = sum(arr, i);
		if (min > gl)
			min = gl;
	}
	printf("min = %d", min);
	return 0;
}
