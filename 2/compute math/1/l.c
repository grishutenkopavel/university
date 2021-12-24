#include <stdio.h>
#include <math.h>
#define Ep 0.001
#define e 2.7182818
// i = integr(sin(x)/(2*cos(x^e)) от 1.8 до 2.1)
//метод прямоугольников правых частей
float rectangle_r(){
    float a = 1.8, b = 2.1, sum = 0,  n = 100, h;
    h = (a+b)/n;
    for(float i = a+h; i <= b; i = i + h)
    {
        sum += sin(i)/(2*cos(pow(i,e)));
    }
    sum *= h;
    printf("%f\n", sum);
    return 0;
}
//метод прямоугольников левых частей
float rectangle_l(){
    float a = 1.8, b = 2.1, sum = 0,  n = 100, h;
     h = (a+b)/n;
    for(float i = a; i <= b - h; i = i + h)
    {
        sum += sin(i)/(2*cos(pow(i,e)));
    }
    sum *= h;
    printf("%f\n", sum);
    return 0;
}
//метод трапеций
float trapeze(){
    float a = 1.8, b = 2.1, sum = 0,  n = 100, h;
    h = (a+b)/n;
    for(float i = a; i <= b-h; i = i + h)
    {
        sum += (sin(i)/(2*cos(pow(i,e)))+sin(i+h)/(2*cos(pow(i+h,e))))/2;
    }
    sum *= h;
    printf("%f\n", sum);
    return 0;
}
//метод Симпсона (парабол)
float simp(){
    float a = 1.8, b = 2.1, sum = 0, sum2 = 0,  n = 10000, h, h2;
    h = (a+b)/n*2;
    h2 = h/2;
    for(float i = a+h2; i <= b-h2; i = i + h)
    {
        sum += sin(i)/(2*cos(pow(i,e)));
    }
    sum = sum * 2;
    for(float i = a+h; i <= b-h; i = i + h)
    {
        sum2 += sin(i)/(2*cos(pow(i,e)));
    }
    sum += sin(a)/(4*cos(pow(a,e)))+sin(b)/(4*cos(pow(b,e)))+sum2; 
    sum = sum * h/3;
    printf("%f\n", sum);
    return 0;
}
//метод двойного пересчета
float method_one(){
    float a = 1.8, b = 2.1, n = 100, h = sqrt(Ep), integ1, integ2;
    do{
        integ1 = 0;
        integ2 = 0;
    for(float i = a; i <= b-h; i = i + h)
    {
        integ1 += (sin(i)/(2*cos(pow(i,e)))+sin(i+h)/(2*cos(pow(i+h,e))))/2;
    }
        integ1 *= h;
        h /= 2;
   for(float i = a; i <= b-h; i = i + h)
    {
        integ2 += (sin(i)/(2*cos(pow(i,e)))+sin(i+h)/(2*cos(pow(i+h,e))))/2;
    }
        integ2 *= h;
    }while(fabs(integ1-integ2) >= Ep);
    printf("%f\n", integ1);
    return 0;
}
//метод 
float method_two(){
    
    return 0;
}
int main(){
    int  choice = 0;
    while(choice != 3){
        printf("Главное меню:\n  1. Метод Ньютона\n  2. Метод дихотомии\n  3. Выход из программы\n");
        scanf("%d", &choice);
        switch (){
            case 1: newton();
                break;
            case 2: dihitam();
                break;
            case 3: return 0;
                break;
            default: printf("Нет такого пункта\n");
        }
    }
    return 0;
}