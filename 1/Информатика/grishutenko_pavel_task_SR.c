/*Расположить на шахматной доске 8x8 случайным образом 2 ладьи так, чтобы они не угрожали друг другу.*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//выделение памяти 
int** create_board(int** board, int* size_b){
	board = (int **) malloc((*size_b)*sizeof(int *)); 
	for (int i=0; i<(*size_b); i++)
  		board[i] = (int *) malloc((*size_b)*sizeof(int));
	return board;
 }
//функция очищает шахматную доску (доска заполняется нулями)
void clear_board(int** board, int* size_b){
	for(int i=0; i<(*size_b); i++)
		for(int j=0; j<(*size_b); j++)
			board[i][j] = 0; //нулем обозначена чистая клетка на которую фигура попасть не может
 }
//демонстрация доски
void show_board(int** board, int* size_b){
	for(int i=0; i<(*size_b); i++){
		for(int j=0; j<(*size_b); j++)
			printf("%d ", board[i][j]);
		printf("\n");
	}
	printf("\n");
 }
// функция для размещения первого слона
int** first_elephant(int** board, int* size_b){
	// установка первой фигуры
	int i = rand() % (*size_b);
	int j = rand() % (*size_b);
	board[i][j] = 2; // двойка означает присутствие слона на клетке
	//выделение позиций куда фигура может двигаться
	for (int k = 0; k < (*size_b); k++)
		if(2 != board[i][k])
			board[i][k] = 1; //единицей обозначается клетка на которую может попасть фигура
	for (int k = 0; k < (*size_b); k++)
		if(2 != board[k][j])
			board[k][j] = 1; //единицей обозначается клетка на которую может попасть фигура
	return board;
 }
// функция для размещения второго слона
void second_elephant(int** (*fir_fig_position)(int**,int*), int** board, int* size_b){
	board = fir_fig_position(board, size_b); // получение доски с первой фигурой
	// установка второй фигуры
	int i, j;
	for(;;){
	i = rand() % (*size_b);
	j = rand() % (*size_b);
	if (board[i][j] == 0){
		board[i][j] = 2;
		break;
		}
	}
	//выделение позиций куда фигура может двигаться
	for (int k = 0; k < (*size_b); k++)
		if(2 != board[i][k])
			board[i][k] = 1; //единицей обозначается клетка на которую может попасть фигура
	for (int k = 0; k < (*size_b); k++)
		if(2 != board[k][j])
			board[k][j] = 1; //единицей обозначается клетка на которую может попасть фигура			
	}
//в функции расставляется две ладьи
void set_board(int** board, int* size_b){
	void (*set)(int** (*fir_fig_position)(int**,int*), int**, int*); //инициализация ptr на second_elephant()
	set = second_elephant;//указатель на функцию устанавливающую вторую фигуру
	set(first_elephant, board, size_b); //установка двух фигур
 }

//освобождение памяти
void free_mem(int** board, int* size_b){
	for(int i = 0; i < (*size_b); i++)
		free(board[i]);	
	free(board);
	}
int main(void){
	int size = 8;
	int **board; 
	srand(time(NULL));
	board = create_board(board, &size); //создание доски
	clear_board(board, &size); //заполнение доски нулями
	show_board(board, &size); //отображение пустой доски
	set_board(board, &size);//размещение двух фигур на доске
	show_board(board, &size); //отображение текущего состояния доски
	clear_board(board, &size); //заполнение доски нулями
	set_board(board, &size); //размещение двух фигур на доске
	show_board(board, &size); //отображение текущего состояния доски
	free_mem(board, &size); //освобождение памяти
	return 0;
 }
