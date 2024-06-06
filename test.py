
from bloom_filter.bloom_filter import BloomFilter


def test_bloom_filter():
    m = 11
    hash_functions = [lambda x: (3*x)%m, lambda x: (2*x)%m]
    bf = BloomFilter(m, hash_functions)
    keys = [7, 12, 9]
    print("Before adding keys:")
    print(bf.as_register_string())
    for key in keys:
        print("Adding key:", key)
        bf.add(key)
        print(bf.as_register_string())
    
    keys_to_lookup = [7, 8, 5]
    for key in keys_to_lookup:
        print("Looking up key:", key)
        print(bf.lookup(key))
    

def main():
    test_bloom_filter()

if __name__ == "__main__":
    main()