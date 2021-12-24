#include <stdio.h>
#include <math.h>

double integr(double r){
    double rzem = 6.377, r1=60.27*rzem, r2=r1+rzem, g=3070/r2*r2, t;
    return sqrt((r1*r2)/(2*g*rzem*rzem*(r2-r1))); //подинтегральная функция
}

double solve(double r1, double r2, double g, double rzem)
{
    //todo решение интеграла
    
    double a = r1, b = rzem, h, n = 20040, s = 0;

    h = (a+b)/n;
    for(double i = a-h; i >= b; i = i - h)
    {
        s += (integr(i) + integr(i+h))/2;
    }
    s *= h;
    return s;
}


int main()
{
    double rzem = 6.377, r1=60.27*rzem, r2=r1+rzem, g=0.2/r2*r2, t;
    t = solve(r1, r2, g, rzem);
    //t = (r1*r2)/(2*g*rzem*rzem*(r2-r1));
    printf("%g", t);
    return 0;
}