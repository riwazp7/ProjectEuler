#include <stdio.h>


int calculate(){
	int x,y,z;
	for (x=100; x<=500; x++){

		for (y=100; y<=500; y++){
		  
			for (z = 100; z<=500; z++){

			  if ((x+y+z) == 1000 && (x*x + y*y == z*z))  {

			    return x*y*z;
			    
				        
				}
			}
		}
	}
	
return -1;

}

int main() {
	
	printf("%d\n", calculate() );

}

