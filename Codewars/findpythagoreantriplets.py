# find all pythagorean triplets under given value n
# pythagorean triplets are defined as {x,y,z}| 1 <= x,y,z <= n , x^2 + y^2 = z^2
# implementation using map and filter

def setPythagoreanTriplet(n):
    return [(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x * x + y * y == z * z]


if __name__ == '__main__':
    print(setPythagoreanTriplet(16))
