#include <stdio.h>
#include <stdlib.h>

double square(double num){
    double result = num * num;
    return result;
}

int main(){
    double x = 3; 
    double y = square(x);
    printf("%.1lf", y);
    return 0;
}
 