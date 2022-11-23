import math
class My_dataStructure:
    def __init__(self, capacity, time = 0): # initialize the data structure
        self.capacity = capacity # capacity of the cache
        self.time = time    # current time
        self._dict = {} # we use dictionary to store the key-value pairs, this is basically hash table implementation in python
        self.count = 0 # number of key-value pairs in the cache
    def get(self, key): # get the value
        self.time += 1  # update the time
        if key in self._dict:
            return self._dict[key][0]
        else:
            return -1 
    def score(self, key):   # calculate the score of a key as given in the problem
        if key in self._dict:
            if self.time != self._dict[key][2]:
                score = self._dict[key][1] / math.log(self.time - self._dict[key][2] + 1)
            else:
                score = self._dict[key][1] / -100
            return score
        else:
            return -1
    def put(self, key, value, weight):  # put the key-value pair into the cache
        self.time += 1
        if key in self._dict: # set the value
            last_access_time = self.time
            self._dict[key] = [value,weight,last_access_time]   # update the value, weight and time accordingly
        else:
            if self.count < self.capacity: #inserting a new key-value
                self._dict[key] = [value,weight,self.time]
                self.count += 1
            else: # replace the least score key-value
                # for this we find the key with minimum score
                min_score_key = min(self._dict.keys(), key = lambda x: self.score(x))   # find the key with minimum score
                self._dict[min_score_key] = [value,weight,self.time]
    def __str__(self):
        return str(self._dict)