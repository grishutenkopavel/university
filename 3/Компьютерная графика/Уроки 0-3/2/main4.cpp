#include <iostream>
#define GRAVITY 9.8
double getHeight()
{
    double towerHeight;
    std::cout << "Enter height of the tower in meters: ";
	std::cin >> towerHeight;
	return towerHeight;
}
double calculateHeight(double towerHeight, int seconds)
{
	
	double distanceFallen = (GRAVITY * seconds * seconds) / 2;
	double currentHeight = towerHeight - distanceFallen;
 
	return currentHeight;
}
void printHeight(double currentHeight, int seconds)
{
	if (currentHeight > 0.0)
		std::cout << "At " << seconds << " seconds, the ball is at height: " << currentHeight << " meters\n";
	else
		std::cout << "At " << seconds << " seconds, the ball is on the ground.\n";
}
int main()
{
	const double towerHeight = getHeight();
 
	printHeight(calculateHeight(towerHeight, 0), 0);
	printHeight(calculateHeight(towerHeight, 1), 1);
    printHeight(calculateHeight(towerHeight, 2), 2);
    printHeight(calculateHeight(towerHeight, 3), 3);
    printHeight(calculateHeight(towerHeight, 4), 4);
    printHeight(calculateHeight(towerHeight, 5), 5);
	return 0;
}