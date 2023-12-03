
class Iloc(dict):
    def __init__(self, dictionary: dict):
        self.sdict = dictionary

    @property
    def sorted_keys(self):
        return list(sorted(self.sdict.keys()))

    def __getitem__(self, idx):
        if not isinstance(idx, int):
            raise TypeError("The index should be a number")
        if idx < 0 or idx > len(self.sdict):
            raise ValueError("The index extends beyond the boundaries of the dictionary")
        return self.sdict[self.sorted_keys[idx]]
        
        
        