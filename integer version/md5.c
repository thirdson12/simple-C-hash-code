#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

unsigned int hash_function(const char* str, int m) {
    unsigned char md5_digest[MD5_DIGEST_LENGTH];
    MD5((const unsigned char*) str, strlen(str), md5_digest);

    unsigned int hash = 0;
    for (int i = 0; i < 2; i++) {
        hash = (hash << 8) + md5_digest[i];
    }
    return hash % m;
}

int main() {
    int m = 10000;
    const char* str = "hello world";
    unsigned int hash = hash_function(str, m);
    printf("Hash value: %u\n", hash);
    printf("Hash value: %x\n", hash);
    return 0;
}
