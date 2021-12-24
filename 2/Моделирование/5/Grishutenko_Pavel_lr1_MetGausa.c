#include <stdio.h>
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
    float a_ii, v;
    for(int i = 0; i < _i-1; i++)
    {   
        a_ii = array[i][i];
        for(int j = i; j < _j; j++)
                {
                    array[i][j] = array[i][j] / a_ii;
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
    /*вывод матрицы 
    for (int i=0; i<_i; i++){
        for (int j=0; j<_j; j++)
            printf("%f ", array[i][j]);
        printf("\n");
    }*/

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