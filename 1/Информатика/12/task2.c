#include <graphics.h>
#include <conio.h>
#include <stdio.h>
int main(void)
{
int GrDr,GrMod,rez ;
GrDr=DETECT ;
initgraph(&GrDr,&GrMod, 0) ;
rez=graphresult() ;
if(rez != grOk)
{
printf("\n ������ ������������� �������") ; return(0) ;
} /* ���. if */
line(0,0,100,100) ;
getch() ;
closegraph() ;
return(1) ;
} /* ���. main() */