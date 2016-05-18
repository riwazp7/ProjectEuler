/* Euler45.c
 * (c) 2016 (yay first line of 2016 code that is not css/html in this file) Riwaz Poudyal
 * secs
 */

#include <stdio.h>
#include <math.h>


long isHexagonal( long n){
  long x = (long) sqrt( (float) (1 + 8 *  n));
    if ( ((x * x) == (1 + 8 * n) ) && ( ! ((x + 1) % 4) )) return x;
  return 0;
}

long isPentagonal(long n){
  long x = (long) sqrt ( (float) ( n * 24 + 1 ));
  if ( ((x * x) == (n * 24 + 1) ) && ( ! ((x + 1) % 6) )) return x;
  return 0;

}

long isTriangular(long n){
  long x = (long) sqrt ( (float) ( n * 8 + 1 ));
  if ( ((x * x) == (n * 8 + 1) ) && ( ! ((x - 1) % 2) )) return x;
  return 0;

}

int main() {

  //printf("%d\n", isPentagonal(40755));
  long n = 40755;
  while ( ! (isHexagonal(n++) && isPentagonal(n) && isTriangular(n))) if (n%1000000 == 0) printf("%ld\n",n);
  printf("%ld\n", n);

}

