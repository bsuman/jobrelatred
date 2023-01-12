# Enter your code here. Read input from STDIN. Print output to STDOUT
class EvenStream:
    def __init__(self):
        self.even = 0

    def get_next(self):
        val = self.even
        self.even = self.even + 2
        return val


class OddStream:
    def __init__(self):
        self.odd = 1

    def get_next(self):
        val = self.odd
        self.odd = self.odd + 2
        return val


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for val in range(int(n)):
        print(stream.get_next())


q = input()
inline = []
for i in range(int(q)):
    instr = input()
    inline.append(instr)

for instr in inline:
    splistr = instr.split(' ')
    if splistr[0] == 'even':
        print_from_stream(splistr[1])
    else:
        print_from_stream(splistr[1], OddStream())
