class LFUCache:
    def __init__(self, capacity: int):
        if capacity > 0:
            self.c_dict = {}
            self.v_dict = {}
            self.capacity = capacity
        else:
            print("Capacity of LFU Cache must be > 0!")

    def get(self, key: int) -> int:
        try:
            val = self.v_dict[key]
            del self.v_dict[key]
            self.v_dict[key] = val
            self.c_dict[key] = self.c_dict[key] + 1
            return val
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            del self.v_dict[key]
            self.v_dict[key] = value
            self.c_dict[key] = self.c_dict[key] + 1
        except KeyError:
            if len(self.v_dict.items()) == self.capacity:
                if self.capacity == 1:
                    del self.v_dict[list(self.c_dict.keys())[0]]
                    del self.c_dict[list(self.c_dict.keys())[0]]
                else:
                    self.c_dict = dict(sorted(self.c_dict.items(), key=lambda x: x[1]))
                    if self.c_dict[list(self.c_dict.keys())[0]] < self.c_dict[list(self.c_dict.keys())[1]]:
                        del self.v_dict[list(self.c_dict.keys())[0]]
                        del self.c_dict[list(self.c_dict.keys())[0]]
                    elif self.c_dict[list(self.c_dict.keys())[0]] == self.c_dict[list(self.c_dict.keys())[1]]:
                        del self.c_dict[list(self.v_dict.keys())[0]]
                        del self.v_dict[list(self.v_dict.keys())[0]]

            self.v_dict[key] = value
            self.c_dict[key] = 1


if __name__ == "__main__":
    lfu = LFUCache(3)
    lfu.put(2, 2)  # cache = [1, _], cnt(1) = 1
    lfu.put(1, 1)  # cache = [2, 1], cnt(2) = 1, cnt(1) = 1
    lfu.put(3, 3)  # 2 is the LFU key because cnt(2) = 1 is the smallest, invalidate 2. cache = [3, 1], cnt(3) = 1, cnt(1) = 2
    lfu.put(4, 4)
    print(lfu.get(3))  # return -1(not found)
    print(lfu.get(2))  # return 3 cache = [3, 1], cnt(3) = 2, cnt(1) = 2
    print(lfu.get(1))  # return -1(not found)
    print(lfu.get(4))  # return 3 // cache = [3, 4], cnt(4) = 1, cnt(3) = 3
