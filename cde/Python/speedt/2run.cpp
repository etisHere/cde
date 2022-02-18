#include <stdlib.h>
#include <stdio.h>

int main(){
	char test = system("time ./t1 && time ./t2 && time python t3.py");
	printf("DONE\n");
	return 0;
}
