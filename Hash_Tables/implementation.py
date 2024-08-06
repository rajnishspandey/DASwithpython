class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(self.size)]

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        return hash

    def set(self, key, value):
        hash_key = self._hash(key)
        # Check if the key already exists and update it
        for pair in self.data[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        # If the key does not exist, add a new key-value pair
        self.data[hash_key].append([key, value])

    def get(self, key):
        hash_key = self._hash(key)
        # Find the key in the bucket
        for pair in self.data[hash_key]:
            if pair[0] == key:
                return pair[1]
        return None

    def keys(self):
        # Collect all keys from all buckets
        keys_array = [pair[0] for bucket in self.data for pair in bucket]
        return keys_array

    def values(self):
        # Collect all values from all buckets
        values_array = [pair[1] for bucket in self.data for pair in bucket]
        return values_array

# Example usage
hash_table = HashTable(10)
print(hash_table.data)
hash_table.set('apple', 1)
hash_table.set('banana', 2)
print(hash_table.get('apple'))  # Output: 1
print(hash_table.keys())        # Output: ['apple', 'banana']
print(hash_table.values())      # Output: [1, 2]
