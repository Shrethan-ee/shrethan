#include <stdio.h>


int main() {

    int x2 = 2, y2 = 3;
    int x3 = 7, y3 = 8;
    int x1 = 4, y1 = 5;

   
    int m = x1 - x2; 
    int n = x3 - x1; 

    FILE *file = fopen("output.txt", "w");


      if ((y1 - y2) * n != (y3 - y1) * m) {
        fprintf(file, "The point does not divide the line segment in a constant ratio.\n");
    } else {
        fprintf(file, "%d:%d\n", m, n);
    }
    fclose(file);

    return 0;
}
