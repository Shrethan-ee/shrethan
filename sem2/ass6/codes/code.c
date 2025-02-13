#include <stdio.h>
#include <stdlib.h>
#include <openssl/rand.h>

// Function to generate a random Bernoulli trial for probability p
int random_number(double p) {
    unsigned char random_byte;
    if (RAND_bytes(&random_byte, 1) != 1) {
        fprintf(stderr, "Error generating random byte\n");
        exit(1);
    }
    double random_value = random_byte / 256.0; // Scale to [0,1)
    return random_value < p ? 1 : 0; // Return 1 if event occurs, 0 otherwise
}

// Function to estimate probability of A' ∩ B'
double complement_probability(double p_a, double p_b, double p_a_p_b, int n) {
    int count_A_not_B_not = 0;

    for (int i = 0; i < n; i++) {
        int A = random_number(p_a);
        int B = random_number(p_b);
        int AB = random_number(p_a_p_b);

        int A_union_B = A || B; // A ∪ B
        if (!A_union_B) { // A' ∩ B'
            count_A_not_B_not++;
        }
    }
    return (double)count_A_not_B_not / n;
}

