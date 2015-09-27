/*
 *  Use Math instead: 2*2*2*2*3*3*5*7*11*13*17*19
 *  All the prime numbers needed to form each no. from 2 to 20
 */

#include <stdio.h>

int main(){
	int count = 2521;
	while(1){
		if (count % 10000 == 0) printf("%d\n", count);
		int i, flag = 1;
		for ( i = 20 ; i > 10 ; i--){

			if (! (count % i == 0))
				flag = 0;
				break;
		}

		if (flag) {

			printf("%d\n", count);
			break;
		}

		count++;

	}
}
