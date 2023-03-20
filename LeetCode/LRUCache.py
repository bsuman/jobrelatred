class LRUCache:

    def __init__(self, capacity: int):
        if capacity > 0:
            self.c_capacity = capacity
            self.c_dict = {}
            self.d_list = []
        else:
            print("Error_size_value")

    def get(self, key: int) -> int:
        if key in self.c_dict.keys():
            pos = self.c_dict[key]
            val = self.d_list.pop(pos)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.c_dict.keys():
            pos = self.c_dict[key]
            self.d_list[pos] = value
        else:
            if len(self.d_list) == self.c_capacity:
                key_to_remove = self.d_list.pop(0)
                try:
                    self.c_dict.pop(key_to_remove)
                except KeyError:
                    pass

            pos = len(self.d_list)
            self.d_list.append(value)
            self.dict[key] = pos
