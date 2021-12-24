#include <stdio.h>
int num_max(int *arr){
    int i, num;
    num = arr[0];
    for(i = 0; i<8; i++) 
        if(arr[i]>num)
            num = arr[i];
    return num;
}
int main(){
    int sum=0;
    int a[8] = {1, -5, 4, 2, -4, -5, -3, 6},
        b[8] = {0, -8, 11, -7, -6, 3, 2, 0};
    sum += num_max(a);
    sum += num_max(b);
    printf("%d\n", sum);
    return 0;
}