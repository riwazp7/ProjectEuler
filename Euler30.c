#include <stdio.h>


int main(){
  int temp;
  int i = 10;
  int s = 0;
  while(i < 500000){
    
    int n = i;
    int sum = 0;
    
    while (n){
      
      temp = n % 10;
      sum += (temp * temp * temp * temp * temp);
      n /= 10;
    }
    
    
    if (sum == i) {
      
      s += i;
      printf("%d\n", s);

    }
    
    

    i++;

  }

  return 0;

}
