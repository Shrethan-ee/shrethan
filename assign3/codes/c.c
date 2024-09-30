#include <stdio.h>

int main() {
    // Normal vector of the line 2x + 5y = 0
    int normal_x = 2;
    int normal_y = 5;

    // Direction vector, which is perpendicular to the normal vector
    int direction_x = -5;
    int direction_y = 2;

    // Open the file to write the output
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the vectors to the file
    fprintf(file, "Normal vector: <%d, %d>\n", normal_x, normal_y);
    fprintf(file, "Direction vector: <%d, %d>\n", direction_x, direction_y);

    // Close the file
    fclose(file);

    // Inform the user that the output has been saved
    printf("Vectors saved to output.txt\n");

    return 0;
}

