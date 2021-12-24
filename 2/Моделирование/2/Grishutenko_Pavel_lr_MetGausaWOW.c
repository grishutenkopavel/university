#include <stdio.h>
#include <math.h>
#define _i 4
#define _j 5
void solve(float *a, float *b){
    //создание одной матрицы
    float array[_i][_j];
    int count_a = 0, count_b = 0;
    for(int i = 0; i < _i; i++){
        for(int j = 0; j < _j-1; j++){
            array[i][j] = a[count_a];
            count_a++;
        }
        array[i][_j-1]=b[count_b];
        count_b++;
    }
    //решение задачи
    float a_max, v, max, tmp;
    int max_j;
    
    //Выбор максимального элемента и замена столбцов
    for (int j = 0; j < _j-2; j++)
    {   
        max_j = j;
        max = array[0][max_j];
        for(int s = j + 1; s<_j-2;s++)
        {
            if (max < array[0][s])
                max_j = s;
        }
        for (int i = 0; i < _i; i++)
        {
            tmp = array[i][j];
            array[i][j] = array[i][max_j];
            array[i][max_j] = tmp;
        }
    }

    //вывод матрицы 
    for (int i=0; i<_i; i++){
        for (int j=0; j<_j; j++)
            printf("%f ", array[i][j]);
        printf("\n");
    }
    for(int i = 0; i < _i-1; i++)
    {   
        
        //прямой ход
        a_max = array[i][i];
        for(int j = i; j < _j; j++)
        {
            array[i][j] = array[i][j] / a_max;
        }
        
        for(int k = i + 1; k <_i; k++)
        {   
            v = array[k][i];
            for(int j = 0; j < _j; j++)
            {
                array[k][j] -= v * array[i][j];
            }
        }

    }
    // v -> копит сумму
    v = 0;
    for(int i = _i-1; i >= 0; i--)
    {
        for(int j = _j-2; j > i; j--)
        {
            v += array[i][j]*array[j][j];
        }
        array[i][i] = (array[i][_j-1]-v)/array[i][i];
        v = 0;
        printf("x%d = %f\n", i+1, array[i][i]);
    }
    //вывод матрицы 
    for (int i=0; i<_i; i++){
        for (int j=0; j<_j; j++)
            printf("%f ", array[i][j]);
        printf("\n");
    }

}

int main(){

    float a[_i][_j-1]={{5, 7, 6, 5},
                 {7, 10, 8, 7},
                 {6, 8, 10, 9},
                 {5, 7, 9, 10}};
    float b[_i][1]={{23}, {32}, {33}, {31}};
    solve(&a[0][0], &b[0][0]);
    return 0;
}
