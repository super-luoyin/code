class SumString:
    def __init__(self, *rags):
        self.values = [x for x in rags]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]


a = SumString(1,2,3,4,5)
print(a[1])
print(a.count)
