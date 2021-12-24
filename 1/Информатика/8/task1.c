#include <stdio.h>
int get_unsum(int *arr, int num){
    int i, sum=0;
    for(i = 0; i<num; i++) 
        if(arr[i]>0)
            sum += arr[i];
    return sum;
}
int main(){
    int a[6] = {1, 5, -4, 2, -6, 6},
        b[8] = {0, 0, -3, -1, 10, 3, 2, 0}, 
        c[7] = {4, -5, -8, 11, -7, -6, 3};
    printf("%d\n",get_unsum(a, 6));
    printf("%d\n",get_unsum(b, 8));
    printf("%d\n",get_unsum(c, 7));
    return 0;
}