#include <stdio.h>
void two_num(int (*arr)[3]){
    int i, j, m, n;
    for(i=0; i < 3; i++){
	for(j=0; j < 3; j++){
            n = j;
            for(m=i; m<3; m++){
                for(n; n<3; n++)
                   if((arr[i][j]==arr[m][n]) && !(i == m && j == n))
                       printf("%d ", arr[i][j]);
            n = 0;       
            }          
        }
    }
}
int main(){
    int s[3][3] = {{1, -5, 1},
                   {3, -8, -5}, 
                   {-3, 4, 5}},
        k[3][3] = {{0, 7, 1},
                   {7, 9, -6}, 
                   {-3, 2, 0}};
    two_num(s);
    printf("\n");
    two_num(k);
    return 0;
}