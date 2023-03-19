
#include <stdio.h>

unsigned int hash_function(const char* str, int m) {
    unsigned int hash = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        hash = hash * 7 + str[i];
    }
    return hash % m;
}

int main()
{
    int m = 10000;
    const char* str = "hello sdjhaknnhnhnhnhnsgdk";
    unsigned int hash = hash_function(str, m);
    printf("Hash value: %d\n", hash);
    printf("Hash value: %x\n", hash);
    return 0;
}


