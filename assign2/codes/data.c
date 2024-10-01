#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"

int main() {

    int x2 = 2, y2 = 3;
    int x3 = 7, y3 = 8;
    int x1 = 4, y1 = 5;

   
    int m = x1 - x2; 
    int n = x3 - x1; 

    FILE *file = fopen("output.txt", "w");

    
    fprintf(file, "\\documentclass{article}\n");
    fprintf(file, "\\begin{document}\n");

      if ((y1 - y2) * n != (y3 - y1) * m) {
        fprintf(file, "The point does not divide the line segment in a constant ratio.\n");
    } else {
        fprintf(file, "%d:%d.\n", m, n);
    }

    fprintf(file, "\\end{document}\n");

    fclose(file);

    return 0;
}
