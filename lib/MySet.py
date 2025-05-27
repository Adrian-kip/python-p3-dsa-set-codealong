class MySet:
    def __init__(self, enumerable=None):
        self.dictionary = {}
        if enumerable is not None:
            for value in enumerable:
                self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def __str__(self):
        return f"MySet: {{{', '.join(str(key) for key in self.dictionary.keys())}}}"