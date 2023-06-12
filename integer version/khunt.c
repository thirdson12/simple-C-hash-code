#include <stdio.h>
#include <stdint.h>

uint16_t hash_function(const char* str, int m) {
    uint16_t hash = 0; //2-byte
    for (int i = 0; str[i] != '\0'; i++) {
        hash = hash * 33 + str[i];
    }
    hash = (hash * (hash + 3)) % m; // Modified Knuth variant on division
    return hash;
}

int main()
{
    int m = 10000;
    const char* str = "hello sdjhaknnhnhnhnhnsgdk";
    uint16_t hash = hash_function(str, m);
    printf("Hash value: %u\n", hash);
    printf("Hash value: %x\n", hash);
    return 0;
}