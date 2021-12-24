#include <stdio.h>
#define _i 4
#define _j 5
void solve(float *a, float *b){
    //создание одной матрицы array
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
    //прямой ход получаем треугольную матрицу
    float a_ii, kf;
    for(int i = 0; i < _i-1; i++)
    {   
        a_ii = array[i][i];
        for(int j = i; j < _j; j++)
        {
            array[i][j] = array[i][j] / a_ii;
        }
        for(int k = i + 1; k <_i; k++)
        {   
            kf = array[k][i];
            for(int j = 0; j < _j; j++)
            {
                array[k][j] -= kf * array[i][j];
            }
        }
    }
    kf = 1/array[_i-1][_j-2];
    for(int j = _j-2; j<_j;j++)
        array[_i-1][j]*=kf;

    //обратный ход получаем единичную матрицу матрицу
    for(int i = _i-1; i > 0; i--)
    {

        for (int k = i-1; k > -1; k--)    
        {   
            kf = array[k][i]/array[i][i];
            for(int j = 0; j < _j; j++)
            {
                array[k][j] -= kf * array[i][j];
            }
        }
        
    }
    //вывод ответа
    for (int i=0; i<_i; i++){
        printf("X%d = %f ",i+1, array[i][_j-1]);
        printf("\n");
    }
    //вывод матрицы 
    // for (int i=0; i<_i; i++){
    //     for (int j=0; j<_j; j++)
    //         printf("%f ", array[i][j]);
    //     printf("\n");
    // }

}

int main(){

    float a[_i][_j-1]={{1, 0, 0, 1},
                       {-1, 1, 0, 1},
                       {0, -1, 1, 1},
                       {0, 0, -1, 1}};
    float b[_i][1]={{10}, {-0.1}, {0.1}, {-0.1}};
    solve(&a[0][0], &b[0][0]);
    return 0;
}
