
import hashlib
import zlib

def md5_hash(str, m):
    md5_digest = hashlib.md5(str.encode()).digest()
    hash = 0
    for i in range(2):
        hash = (hash << 8) + md5_digest[i]
    return hash % m

def sha256_hash(str, m):
    sha256_digest = hashlib.sha256(str.encode()).digest()
    hash = 0
    for i in range(2):
        hash = (hash << 8) + sha256_digest[i]
    return hash % m

def crc32_hash(str, m):
    crc32_digest = zlib.crc32(str.encode()).to_bytes(4, byteorder='little')
    hash = 0
    for i in range(2):
        hash = (hash << 8) + crc32_digest[i]
    return hash % m

input_str = input("Enter a string: ")
m = int(input("Enter the size of the hash table: "))

md5 = md5_hash(input_str, m)
sha256 = sha256_hash(input_str, m)
crc32 = crc32_hash(input_str, m)

print(f"MD5 Hash: {md5}")
print(f"SHA256 Hash: {sha256}")
print(f"CRC32 Hash: {crc32}")