//задача 2
#include <stdio.h>
#include <math.h>
float sum(float r[], int x){
    float sum = 0;
    for (int i = 1; i < x; i++){
        sum += r[i] - r[0];
    }
    return sum;
}
float sum2(float r[], int x){
    float sum = 0;
    for (int i = 1; i < x; i++){
        sum += pow(r[i] - r[0], 2);
    }
    return sum;
}
int main(){
    float r[6] = {7.48, 7.48, 7.49, 7.52, 7.47, 7.5};
    float average, average2, otklonenie, abs_pog, otn_pog;
    average = sum(r, 6) / 5 + r[0];
    average2 = (sum2(r, 6) - 5 * pow(average-r[0], 2))/(5*(5-1));
    otklonenie = sqrt(average2);
    abs_pog = 2.57 * otklonenie;
    otn_pog = abs_pog / average * 100;
    printf("Среднее значение = %g\n", average);
    printf("Средне квадратичная погрешность = %g\n", average2);
    printf("Стандартное отклонение = %g\n", otklonenie);
    printf("Абсолютная погрешность = %g\n", abs_pog);
    printf("Относительная погрешность = %g\n", otn_pog);
}