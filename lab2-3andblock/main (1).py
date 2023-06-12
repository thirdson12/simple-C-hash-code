import hashlib
import zlib

def md5_hash(input_str, m):
    md5_digest = hashlib.md5(input_str.encode()).digest()
    hash_val = int.from_bytes(md5_digest[:2], byteorder='big')
    return hash_val % m

def sha256_hash(input_str, m):
    sha256_digest = hashlib.sha256(input_str.encode()).digest()
    hash_val = int.from_bytes(sha256_digest[:2], byteorder='big')
    return hash_val % m

def crc32_hash(input_str, m):
    crc32_val = zlib.crc32(input_str.encode())
    return crc32_val % m

if __name__ == '__main__':
    input_str = input("Enter a string: ")
    m = 10000
    
    md5_hash_val = md5_hash(input_str, m)
    sha256_hash_val = sha256_hash(input_str, m)
    crc32_hash_val = crc32_hash(input_str, m)
    
    print(f"MD5 Hash Value: {md5_hash_val:04x}")
    print(f"SHA256 Hash Value: {sha256_hash_val:04x}")
    print(f"CRC32 Hash Value: {crc32_hash_val:04x}")
