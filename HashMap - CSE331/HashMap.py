

class HashMap:
    def __init__(self, load_factor=1.00, cap = 20):
        '''
        initalize our map
        :param load_factor: this is the ratio of items to number of available slots in our map
        '''
        # You may change the default maximum load factor
        self.max_load_factor = load_factor
        # Other initialization code can go here
        self._map = [[] for i in range(cap)]
        self._n = 0 #number of entries

    def __len__(self):
        '''
        finds length of our map, from book
        runs in amortized constant time
        :return:
        '''
        return self._n #return size of map

    def load(self):
        '''
        finds the ratio of items in our map to the number of slots, average value per slot
        must be below 1.0 at all times
        runs in amortized constant time
        :return:
        '''

        cur_load =  self._n / len(self._map) #find current load
        if(cur_load <= self.max_load_factor): #if its under our max load, return
            return float(cur_load)
        else:  #if not, resize our hash map
            #resize
            self._map = self.__newHashMap__()
            return float(self._n) / len(self._map)

    def __contains__(self, key):
        """
        determines whether an association with the given key exists, returns false if it doesn't
        runs in amortized constant time
        :param key:
        :return:
        """
        try: #if getitem can obtain key, it exists
            x = self.__getitem__(key)
            return True
        except:  #if unable to, key isn't contained by hash map
            return False

    def __getitem__(self, key):
        '''
        determines which value is associated with a given key
        runs in amortized constant time
        :param key: pass in key we're looking for, if not found raise key error
        :return: returns value types
        '''
        hash = self.__sizeHash__(key)
        bucket = self._map[hash]
        for tup in bucket: #go thru bucket
            if tup[0] == key:  #if key is found return
                return tup[1]  #return item
        raise KeyError  #if not found raise error

    def __setitem__(self, key, value):
        '''
        Assign value to key, overwriting if existing value is present
        adds association to map
        runs in amortized constant time
        :param key:
        :param value:
        :return:
        '''
        hash = self.__sizeHash__(key)
        bucket = self._map[hash]
        for i in range(len(bucket)): #Go thru bucket
            if bucket[i][0] == key:  #find key, if it exists update it
                bucket[i] = (key,value)
                return
        bucket.append((key,value))  #if not add the key to our hash map
        self._n += 1 #add space

    def __delitem__(self, key):
        """
        removes association to map, raise error if not exist
        runs in amortized constant time
        :param key:
        :return:
        """
        hash = self.__sizeHash__(key)
        bucket = self._map[hash]
        for i in range(len(bucket)):  #go thru bucket
            if bucket[i][0] == key:  # see if key exists
                del bucket[i]  #if it does delete it
                self._n -= 1  #fix size
                return
        raise KeyError  #if item doesn't exist, throw error

    def __iter__(self):
        '''
        enumerates each key-value pair
        runs in O(n) time
        :return:
        '''

        for bucket in self._map: #run thru each bucket
            for tup in bucket:  #grab each tuple pair of key-value
                yield tup
    def clear(self):
        """
        removes all key-value pairs from association with map
        runs in O(n) time
        :return:
        """
        for i in range(len(self._map)):  #go thru and make each empty
            self._map[i] = []
        self._n = 0 #number of entries

    def keys(self):
        """
        returns a set of keys that are in the map
        runs in O(n) time
        :return: set of keys
        """
        keys = set()
        for bucket in self._map:  #go thru each bucket
            for tup in bucket:  #grab only keys
                keys.add(tup[0])
        return keys #return keys

    # supplied methods

    def __repr__(self):
        return '{{{0}}}'.format(','.join('{0}:{1}'.format(k, v) for k, v in self))

    def __bool__(self):
        return not self.is_empty()

    def is_empty(self):
        return len(self) == 0



    # Helper functions can go here

    def __sizeHash__(self, key):
        '''
        returns the value to place key in correct bucket
        :param key:
        :return:
        '''
        return hash(key) % len(self._map)  # uses hash function + length of current map to place items

    #take current n * 2
    #Make a new hash map as size of current
    #iterate thru existing one
    #add existing to new hashmap
    #current hashmap = new hashmap
    #use .5 as new reference
    def __newHashMap__(self):
        """
        creates new hash map if our load factor goes over 1.0
        :param key:
        :return:
        """
        hashMap = HashMap(self.max_load_factor, self._n*2)  #make a new hashmap that has a load factor under 1.0
        for tup in self.__iter__(): #copy the items from the original map to new
            hashMap[tup[0]] = tup[1]
        return hashMap._map #return it

# Required Function
def word_frequency(seq):
    """
    takes a sequence of words, returns hash map of each unique word w/ # of times
    it appears in sequence
    runs in O(n) time
    :param seq:
    :return:
    """
    map = HashMap(max_load_factor, self._n)

