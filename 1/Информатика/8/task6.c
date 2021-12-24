#include <stdio.h>
#include <math.h>
void colavg(int (*arr)[5]){
    int i, j;
    float mul=1, avg;
    for(i=0; i < 5; i++){
        for(j=0; j < 3; j++){
               mul *= arr[j][i];
        }
    avg = pow(mul, (float)1/3);
    printf("%g ", avg);       
    mul = 1;
    }
}
int main(){
    int s[3][5] = {{1, 5, 1, 4, 3},
                   {3, 8, 5, 6, 9}, 
                   {3, 4, 5, 1, 2}};
    colavg(s);
    return 0;
}