#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(){
    int nota;
    printf("Please tick off one of the boxes: ");
    scanf("%i", &nota);
    
    switch(nota){
        case 1:
            printf("You got the correct answer! Congrats");
            break;
        case 2:
            printf("You got it wrong.\nStudy harder next time.");
            break;  
        default:
            printf("Please input a valid answer.");                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    };
    return 0;
}
 