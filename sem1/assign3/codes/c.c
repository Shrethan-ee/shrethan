#include <stdio.h>

int main() {
    // Normal vector of the line 2x + 5y = 0
    double normal_x = 2;
    double normal_y = 5;
    
    double n=normal_x/normal_y;
    double m=-n;

    // Open the file to write the output
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the vectors to the file
    fprintf(file, "%.1lf, 1\n", n);
    fprintf(file, "1,%.1lf\n", m);

    // Close the file
    fclose(file);

    // Inform the user that the output has been saved
    printf("Vectors saved to output.txt\n");

    return 0;
}

