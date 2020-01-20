class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""

    def get_table_size(self):
        """ Returns the size of the hash table."""

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""

