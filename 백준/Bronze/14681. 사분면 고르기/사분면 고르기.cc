#include <iostream>

using namespace std;

int main(void){
	int a, b;
	
	scanf("%d %d", &a, &b);
	
	if(a>0 && b>0)
		printf("1");
	else if(a<0 && b>0)
		printf("2");
	else if(a>0 && b<0)
		printf("4");
	else
		printf("3");
}