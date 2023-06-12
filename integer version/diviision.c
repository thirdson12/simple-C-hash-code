#include <stdio.h>

unsigned short hash_function(const char* str, int m) {
    unsigned short hash = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        hash = hash * 7 + str[i];
    }
    return hash % m & 0xFFFF;
}

int main()
{
    int m = 10000;
    const char* str = "hello sdjhaknnhnhnhnhnsgdk";
    unsigned short hash = hash_function(str, m);
    printf("Hash value: %hu\n", hash);
    printf("Hash value: %hx\n", hash);
    return 0;
} 