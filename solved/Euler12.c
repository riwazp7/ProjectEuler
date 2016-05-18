#include <stdio.h>
#include <math.h>
	
int numfac(int num){
	
	int i, count = 0;
	
	for (i = 1; i < (int) sqrt( (double) num) + 1; i++) {

		if (num%i == 0) count++;

	}

	//Factors occur in pairs
	return count*2;

}


int main(int argc, char const *argv[]){
		
	int num, i = 1;

	while (1){

		num = i*(i+1)/2;
		if ( numfac(num) > 500) break;
		i++;
	}

	printf("%d\n", num );

	return 0;
}