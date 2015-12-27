/* Euler27.c
 * (c) 2015 Riwaz Poudyal
 * 0.09 secs
 */


#include <stdio.h>

int isPrime(int n){
  if (n <= 1) return 0; 
  int i;
  for ( i = 2; i*i <= n; i++) if (n % i == 0) return 0;
  return 1;
}


int main(){

  int high_a = 0, high_b = 0, high_n = 0;

  int a, b, n;
  
  for ( a = -1000; a < 1001; a++) {

    for ( b = -1000; b < 1001; b++) {
      
      n = 0;
      
      while (1) {
	
	if ( !isPrime(n * n + a * n + b)) break;
	n++;
      }

      if ( n > high_n ){
	high_a = a;
	high_b = b;
	high_n = n;

      }
    }
  }

  printf("%d\n", high_a * high_b);
  return (0);
}

