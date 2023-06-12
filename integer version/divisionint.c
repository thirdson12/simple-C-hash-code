#include <stdio.h>

unsigned short hash_function(const char* str, int m) {
    unsigned int hash = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        hash = hash * 33 + str[i];
    }
    unsigned short hash_value = (unsigned short)(hash % m); // Basic division method
    return hash_value;
}

int main()
{
    int m = 65521; // Largest prime number that fits into 2 bytes
    const char* str = "hello sdjhaknnhnhnhnhnsgdk";
    unsigned short hash = hash_function(str, m);
    printf("Hash value: %hu\n", hash);
    printf("Hash value: %hx\n", hash);
    return 0;
}
