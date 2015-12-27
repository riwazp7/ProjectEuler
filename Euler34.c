/* Euler34.c
 * (c) 2015 Riwaz Poudyal 
 * 0.008 secs
 */ 


#include <stdio.h>

int main() {

  const int fact [] = {1,1,2,6,24,120,720,5040, 40320, 362880};
  
  int sum = 0, n = 10;

  while (n < 50000) {

    int i = n, s = 0;

    while (i) {

      s += fact[ i % 10];
      i /= 10;

    }

    if ( s == n ) {
      sum += n;
      printf("%d\n", sum);
    }
    n++;
  }


  return(0);

}
