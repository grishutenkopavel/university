#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define _A 0.5
#define _B 1.5
#define _N 100
#define _E 0.0001
#define e 2.71828

void mainmenu();
void first_below_menu();
void second_below_menu();

float integr(float x){
    return sin(pow(x, e))/4; //подинтегральная функция
}
double dif(double x){
    //1/4*e*pow(x, 0.71828)*((1.71828)*cos(pow(x,e))-e*pow(x,e)*sin(pow(x,e)))
    return 0.471*(1.6651-0.678*0.246854);
}
void left_rectangle(){
    float a = _A, b = _B, h, n = _N, s = 0;
    h = (a+b)/n;
    for(float i = a; i <= b - h; i = i + h)
    {
        s += integr(i);
    }
    s *= h;
     printf("%f\n", s);
     first_below_menu();
}
void right_rectangle(){
    float a = _A, b = _B, h, n = _N, s = 0;
    h = (a+b)/n;
    for(float i = a+h; i <= b; i = i + h)
    {
        s += integr(i);
    }
    s *= h;
    printf("%f\n", s);
    first_below_menu();
}
void trapeze(){
    float a = _A, b = _B, h, n = _N, s = 0;
    h = (a+b)/n;
    for(float i = a+h; i <= b; i = i + h)
    {
        s += (integr(i) + integr(i-h))/2;
    }
    s *= h;
    printf("%f\n", s);
    first_below_menu();
}
void parabol(){
   float a = _A, b = _B, h, n = _N, s = 0;
    h = (a+b)/n*2;
    n = 0;
    for(float i = a+h/2; i <= b-h/2; i = i + h)
    {
        s += integr(i);
    }
    s *= 4;
    for(float i = a+h; i <= b-h; i = i + h)
    {
        n += integr(i);
    }
    s += integr(a)+integr(b)+2*n; 
    s *= h/6;
    printf("%f\n", s);
    first_below_menu();    
}
void double_count(){
    float i, a = _A, b = _B, h = sqrt(_E), n = _N, in, in2;
    double r;
    r = fabs(pow(b-a,3)/(12*n*n)*dif(0.6));
    printf("r = %g\n", r);
    do{
        in = 0;
        in2 = 0;
    for(i= a+h; i <= b; i = i + h)
        {
            in += (integr(i) + integr(i-h))/2;
        }
        in *= h;
        h /= 2;
    for(i= a+h; i <= b; i = i + h)
        {
            in2 += (integr(i) + integr(i-h))/2;
        }
        in2 *= h;
    }while(fabs(in-in2)>=_E);
    printf("%f\n", in);
    second_below_menu();
}
void count(){
    exit(0);
}
void first_below_menu(){
    int  choice;
    printf("Методы с постоянным шагом:\n  1. Метод правых частей прямоугольников\n  2. Метод левых частей прямоугольников\n  3. Метод трапеций\n  4. Метод парабол\n  5. Возврат в главное меню\n");
    scanf("%d", &choice);
    switch (choice){
        case 1: right_rectangle();
            break;
        case 2: left_rectangle();
            break;
        case 3: trapeze();
            break;
        case 4: parabol();
            break;
        case 5: mainmenu();
            break;
        default: printf("err: try again\n");
            first_below_menu();
    }
}
void second_below_menu(){
    int  choice;
    printf("Методы с переменным шагом:\n  1. Метод двойного пересчета\n  2. \n  3. Возврат в главное меню\n");
    scanf("%d", &choice);
    switch (choice){
        case 1: double_count();
            break;
        case 2: count();
            break;
        case 3: mainmenu();
            break;
        default: printf("err: try again\n");
        second_below_menu();
    }
}
void mainmenu(){
    int  choice;
    printf("Главное меню:\n  1. Методы с постоянным шагом\n  2. Методы с переменным шагом\n  3. Выход из программы\n");
    scanf("%d", &choice);
    switch (choice){
        case 1: first_below_menu();
            break;
        case 2: second_below_menu();
            break;
        case 3: exit(0);
            break;
        default: printf("err: try again\n");
        mainmenu();
    }

    
}
int main(){
    mainmenu();
    return 0;
}