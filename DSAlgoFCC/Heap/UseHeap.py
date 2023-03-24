import MinHeap as min, MaxHeap as max

if __name__ == '__main__':
    minH = min.MinHeap()
    minH.push(10)
    minH.push(5)
    minH.push(15)
    minH.push(2)
    print(minH.pop())
    print(minH.pop())
    print(minH.pop())
    print(minH.pop())
    print("MAX HEAP")
    maxH=max.MaxHeap()
    maxH.push(10)
    maxH.push(20)
    maxH.push(12)
    maxH.push(15)
    maxH.push(40)

    print(maxH.pop())
    print(maxH.pop())
    print(maxH.pop())
    print(maxH.pop())
