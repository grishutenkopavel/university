#include <iostream>
 
double getDouble()
{
    double x;
    std::cout << "Enter a double value: ";
    std::cin >> x;
    return x;
}
 
char getOperator()
{
    char opr;
    std::cout << "Enter one of the following: +, -, *, / ";
    std::cin >> opr;
    return opr;
}
 
void printResult(double x, double y, char opr)
{
    if (opr == '+')
        std::cout << x << " + " << y << " = " << x + y << '\n';
    else if (opr == '-')
        std::cout << x << " - " << y << " = " << x - y << '\n';
    else if (opr == '*')
        std::cout << x << " * " << y << " = " << x * y << '\n';
    else if (opr == '/')
        std::cout << x << " / " << y << " = " << x / y << '\n';
}
 
int main()
{
    double x = getDouble();
    double y = getDouble();
    char opr = getOperator();
 
    printResult(x, y, opr);
 
    return 0;
}