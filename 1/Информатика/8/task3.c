#include <stdio.h>
#include <math.h>
float get_geomavg(int *arr, float num){
    int i;
    float avg = 1;
    for(i = 0; i<num; i++)
        avg =avg * arr[i];
    num = 1/num;
    avg = pow(avg, num);
    return avg;
}
int main(){
    int a[6] = {1, 5, -4, 2, -6, 6},
        v[8] = {0, 0, -3, -1, 10, 3, 2, 0}, 
        c[7] = {4, -5, -8, 11, -7, -6, 3};
    printf("%g\n",get_geomavg(a, 6));
    printf("%g\n",get_geomavg(v, 8));
    printf("%g\n",get_geomavg(c, 7));
    return 0;
}