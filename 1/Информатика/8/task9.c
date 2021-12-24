#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int** create_matrix(int **matrix, int size_n, int size_m)
{
	matrix = (int**)malloc(size_n * sizeof(int));
	for (int i = 0; i < size_n; i++)
		matrix[i] = (int*)malloc(size_m* sizeof(int));
	return matrix;
} 
void set_matrix(int** matrix, int size_n, int size_m)
{
	for (int i = 0; i < size_n; i++)
		for (int j = 0; j < size_m; j++)
			matrix[i][j] = rand() % 10;

}
void show_matrix(int** matrix, int size_n, int size_m)
{
	for (int i = 0; i < size_n; i++) {
		for (int j = 0; j < size_m; j++) {
			printf("%d  ", matrix[i][j]);
		}
		printf("\n");
	}
}
void free_mem(int** matrix, int size_n)
{
	for (int i = 0; i < size_n; i++)
		free(matrix[i]);
	free(matrix);
}

int main()
{
	srand(time(NULL));
	int size_n, size_m;
	printf("Enter matrix size: ");
	scanf("%d%d", &size_n, &size_m);
	int** matrix;
	matrix = create_matrix(matrix, size_n, size_m);
	set_matrix(matrix, size_n, size_m);
	show_matrix(matrix, size_n, size_m);
	free_mem(matrix, size_n);
	return 0;
}