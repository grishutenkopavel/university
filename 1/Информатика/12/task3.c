#include <graphics.h>
#include <conio.h>
#include <stdio.h>

int main(void)
{
int GrDr,GrMod,rez ;
GrDr=DETECT ;
initgraph(&GrDr,&GrMod, 0) ;
rez=graphresult();
if(rez != grOk)
{
printf("\n Ошибка инициализации графики") ; return(0) ;
} /* Кон. if */
int width = 640, high = 480;
line(width / 2, 0, width / 2, high);
line(0, high / 2, width, high / 2);
int x0 = -15, y0 = x0*x0;
int x1 = -14, y1 = x1 * x1;
for (int i = 0; i < 20; i++) {
	line(width/2 + x0*32, high / 2 - y0*32, width / 2 + x1*32, high / 2 -y1*32);
	x0 = x1;
	y0 = y1;
	x1 = x0 + 1;
	y1 = x1 * x1;
}
getch() ;
closegraph() ;
return(1) ;
} /* Кон. main() */