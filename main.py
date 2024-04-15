class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)


iterable = ["a", "b", "c"]
cyclic_iter = CyclicIterator(iterable)
for _ in range(10):
    print(next(cyclic_iter))
