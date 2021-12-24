#include <stdio.h>
#include <math.h>
#define _A -10
#define _B 10
#define _E 10e-6
//количество точек разбиения 10 50 100
float func(float x){
    return 2*pow(x,4)-8*pow(x,3)+8*x*x-1;
}
float dif(float x){
    return 8*pow(x, 3)-24*x*x+16*x;
}

float newton(){
    float x = (dif(_A)==0)? _B: _A;
    while(fabs(func(x)) > _E){
        x-=func(x)/dif(x);
    }
    printf("x=%f\n",x);
    return 0;
}

int main(){
    int choce = 0;
    while (choce !=4){
        printf("Меню:\n 1. Метод Ньютона\n 2. \n 3. \n");
        scanf("%d", &choce);
    
        switch (choce)
        {
        case 1:
            newton();
            break;
        case 4:
            return 0;
            break;
        default:
            printf("Ошибка. Выбирите другой вариант");
            break;

        }
    }
    return 1;
}