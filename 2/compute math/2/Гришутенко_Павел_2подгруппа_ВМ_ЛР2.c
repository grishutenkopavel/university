//количество разбиений для каждого метода 10, 50, 100
#include <stdio.h>
#include <math.h>
double func(double x, double y)
{
	return y*(1-x); // функция первой производной
}
// функции для диффур второго порядка
double func1(double z, double y)
{
	return y+0.1*z; // функция первой производной
}
double func2(double x, double y, double z)
{
	return z+0.1*(-(z/x+y)); // функция первой производной
}
//функции для системы
double sys1(double x, double z){
    return -2*x+5*z;
}
double sys2(double t, double x, double y, double z){
    return sin(t-1)*x-y-3*z;
}
double sys3(double x, double z){
    return -x+2*z;
}
// методы 
void eler(){
    int i, n; 
    double x, y, h;

    h = 0.01; // шаг
    n = 100; // количество итераций 
    x = 0; // x0
    y = 1; // y0
    for (i = 0; i < n; i++)
    {
        y += h * func(x, y); // вычисление yi
        x += h;
    }
    printf("%g\n", y);
}
void runge_kuta() {
    int i, n; 
    double x, y, h, k1, k2, k3, k4;

    h = 0.01; // шаг
    n = 100; // количество итераций 
    x = 0; // x0
    y = 1; // y0
	for (i = 0; i < n; i++) {
		k1 =  func(x, y);
		k2 =  func(x + h / 2, y + h*k1 / 2);
		k3 =  func(x + h / 2, y + h*k2 / 2);
		k4 =  func(x + h, y + h*k3);
		y = y + h/6*(k1 + 2*k2 + 2*k3 + k4);
		x+=h;
	}
    printf("%g\n", y);
}
void order2(){
    int i, n; 
    double x, y, z, h;

    h = 0.1; // шаг // количество итераций 
    x = 1; // x0
    y = 0.77; // y0
    z = -0.44;
	for (x; x < 1.6; x+=h)
    {
        y = func1(z, y);
        z = func2(x, y, z);
        printf("x = %g y = %g z = %g\n", x, y, z);
    }  
}
void system_equ(){
    int i, n; 
    double x, y, z, t, h;

    h = 0.05; // шаг // количество итераций 
    x = 2; // x0
    y = 1; // y0
    z = 1;
    // t <- [0; 2)
	for (t = 0; t <= 2.05; t+=h)
    {
        x += h*sys1(x, z);
        y += h*sys2(t, x, y, z);
        z += h*sys3(x, z);
        printf("x = %g y = %g z = %g t = %g\n", x, y, z, t);
    }
}
int main() {
    int choice = 1;
    while (choice)
    {
        printf("Меню:\n 1. Метод Эйлера\n 2. Метод Рунге-Кутты\n 3. Дифференциальное уравнение второго порядка\n 4. Система дифференциальных уравнений\n 5. Выход\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1: eler();
            break;
        case 2: runge_kuta();
            break;
        case 3: order2();
            break;
        case 4: system_equ();
            break;
        case 5: return 0;
            break;
        default: 
            printf("Ошибка, нет такого варианта");
            break;
        }
    }
    return 1;
}