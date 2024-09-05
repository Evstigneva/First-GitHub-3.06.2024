class FileReader:
    def __init__(self, filename):
        self.file=open(filename)
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        for i in self.file:
            return i
        
for line in FileReader('lorem.txt'):
    print(line)