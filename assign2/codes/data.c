#include <stdio.h>

int main() {
    // Coordinates of points A, B, and P
    int x2 = 2, y2 = 3;
    int x3 = 7, y3 = 8;
    int x1 = 4, y1 = 5;

    // Calculate the ratio m:n using section formula
    int m = x1 - x2; // m corresponds to (x1 - x2)
    int n = x3 - x1; // n corresponds to (x3 - x1)

    // Open the output.tex file for writing
    FILE *file = fopen("output.txt", "w");

    // Write the LaTeX header
    fprintf(file, "\\documentclass{article}\n");
    fprintf(file, "\\begin{document}\n");

    // The same should hold for y coordinates
    if ((y1 - y2) * n != (y3 - y1) * m) {
        fprintf(file, "The point does not divide the line segment in a constant ratio.\n");
    } else {
        fprintf(file, "The ratio in which P divides AB is %d:%d.\n", m, n);
    }

    // Write the LaTeX footer
    fprintf(file, "\\end{document}\n");

    // Close the file
    fclose(file);

    return 0;
}
