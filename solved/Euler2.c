#include <stdio.h>

//Non recursive implementation
int main(){

  int c, a=1, b=2, sum=2;

  while ((c=a+b) < 4000000){

    if ( c%2 == 0) sum+=c;
    a=b;
    b=c;
  } 
  
  printf("%d\n", sum);
   
}
