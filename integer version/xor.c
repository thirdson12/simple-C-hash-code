#include <stdio.h>
#include <string.h>

unsigned int hash_function(const char* str, int n) {
    unsigned int hash = 0;
    const unsigned char* bytes = (const unsigned char*) str;
    const int block_size = 2;  // block size in bytes
    const int m = n / block_size;  // number of blocks

    for (int i = 0; i < n; i++) {
        const int block_index = i / block_size;
        const int bit_index = i % block_size;

        const unsigned char by = bytes[i];
        const unsigned char bi = (by >> bit_index) & 0x01;

        hash ^= bi << block_index;
    }

    return hash;
}

int main()
{
    const char* str = "hello sdjhaknnhnhnhnhnsgdk";
    unsigned int hash = hash_function(str, strlen(str));
    printf("Hash value: %u\n", hash);
    printf("Hash value: %x\n", hash);
    return 0;
}

