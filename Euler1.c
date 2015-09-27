//Riwaz Poudyal

#include <stdio.h>
int main(){

  //Sum of all multiple of 5 and multiples of 3 upto 199*3
  //without re-adding common ones
  int i, sum = 0;
  for (i = 1; i<200; i++ ) {
    sum+=i*3;
    if (!(i%3==0)) sum+=i*5;
  }

  //Sum of multiples of 3 from 200*3 to 333*3
  for(i = 200; i<=333; i++){
    sum+=i*3;
  }

  printf("%d", sum);
}
