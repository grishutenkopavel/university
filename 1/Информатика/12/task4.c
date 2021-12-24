#include <stdio.h>
#include <graphics.h>
#include <math.h>
#define M_PI 3.1415
int main() {
	int gd = DETECT, gm; initgraph(&gd, &gm, 0);
	setbkcolor(15);
	int midx, midy, color;
	midx = getmaxx();
	midy = getmaxy();
	printf("%d,%d", midx, midy);
	for (color = 0; color <= 15; color++) {
		setcolor(color);
		line(0, 0, getmaxx(), getmaxy());
		circle(getmaxx() / 2, getmaxy() / 2, 50);
		rectangle(10, 10, getmaxx() / 3, getmaxy() / 3);
		ellipse(540, 240, 0, 360, getmaxx() / 15, getmaxy() / 15);
		arc(400, 300, 9, 90, 20);
		getch();
	}
	setfillstyle(SOLID_FILL, 5);
	bar(30, 30, getmaxx() / 4, getmaxy() / 4);
	getch();
	return 0;
}