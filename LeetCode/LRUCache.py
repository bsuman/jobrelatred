class LRUCache:

    def __init__(self, capacity: int):
        if capacity > 0:
            self.c_capacity = capacity
            self.c_dict = {}
        else:
            print("Error_size_value")

    def get(self, key: int) -> int:
        if key in self.c_dict.keys():
            val = self.c_dict[key]
            del self.c_dict[key]
            self.c_dict[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.c_dict.keys():
            del self.c_dict[key]
        else:
            if len(list(self.c_dict.items())) == self.c_capacity:
                key_to_remove = list(self.c_dict.keys())[0]
                del self.c_dict[key_to_remove]
        self.c_dict[key] = value


if __name__ == '__main__':
    lr = LRUCache(3)
    print(lr.get(1))
    for i in range(1, 4):
        lr.put(i, i)
    print(lr.get(1))
    lr.put(4, 4)
    print(lr.get(4))
    print(lr.get(2))
    print(lr.get(3))
    lr.put(5, 5)
    print(lr.get(1))
