#include <stdio.h>
#include <math.h>
#define _E 0.001
ln_function(float x){
    
    return ;
}
arctg_function(float x){
    float result1=0, result2, pow1;
    do{
        result2 = result1;
        result1 += pow(x, pow1)/pow1;
        pow1+=2;
        result1 -= pow(x, pow1)/pow1;
        pow1+=2;
    }while (fabs(result1-result2) <= 0.001);
    return result1;
}
int main(){
    int choice=0;
    float x;
    while(choice!=3){
        printf("Меню:\n 1. ln\n 2. arctg\n 3. Выход\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            //ln_function();
            break;
        case 2: printf("введите x: \n");
                scanf("/f", &x);
                arctg_function(x);
            break;
        case 3:
            return 0;
            break;
        default: printf("выбранного варианта не существует");
            break;
        }
    }

    return 1;
}