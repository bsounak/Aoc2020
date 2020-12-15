import time
import aoc_data

data = aoc_data.load(13).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]
# data = ["939", "7,13,x,x,59,x,31,19"]

# part 1
et = int(data[0])  # earliest timestamp you could depart on a bus
bus_ids = [int(v) for v in data[1].split(",") if not v == "x"]


def get_earliest_bus(ts):
    d = []
    for v in bus_ids:
        if ts % v == 0:
            d.append(0)
        else:
            d.append(v - ts % v)
    return bus_ids[d.index(min(d))], min(d)


v1, v2 = get_earliest_bus(et)
print(v1 * v2)

start = time.time()
# part 2
# This can be solved by chinese remainder theorem
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem

# For example, let's consider data = ["939", "7,13,x,x,59,x,31,19"]
# Bus ids 7,13,59,31,19 have indexes 0,1,4,6,7 respectively. The indexes
# represent the offset of the departures

# We need to find the smallest T, such that
# T % 7 is 0, which is 7-0
# T % 13 is 12, which is 13-1
# T % 59 is 55, which is 59-4
# T % 31 is 25, which is 31-6
# T % 19 is 12, which is 19-7

# To express in terms of congruences
# https://en.wikipedia.org/wiki/Modular_arithmetic
# We need to solve for T such that
# T ≋ 0 (mod 7)
# T ≋ 12 (mod 13)
# T ≋ 55 (mod 59)
# T ≋ 25 (mod 31)
# T ≋ 12 (mod 19)

# The solution for this particular case is T=1068781


def solve_crt(a: list, m: list):
    """
    Solve according to chinese remainder theorem

    Implementation follows this tutorial
    https://www.youtube.com/watch?v=0dbXaSkZ-vc&ab_channel=CenterofMath

    Examples:

    >>> a = [0, 12, 55, 25, 12]
    >>> m = [7, 13, 59, 31, 19]
    >>> solve_crt(a, m)
    1068781

    >>> a = [2, 3, 2]
    >>> m = [3, 5, 7]
    >>> solve_crt(a, m)
    23
    """
    M = 1
    for v in m:
        M *= v
    Mi = [M // m[i] for i in range(len(m))]
    yi = [inverse(Mi[i], m[i]) for i in range(len(m))]

    X = sum([a[i] * Mi[i] * yi[i] for i in range(len(yi))])
    return X % M


def inverse(a: int, n: int):
    """
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers

    Find t such that a*t ≋ 1 (mod n)

    Examples:

    >>> inverse(3, 11)
    4

    which satisfies 3*4 ≋ 1 (mod 11)
    """

    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)

    if r > 1:
        raise Exception("a is not invertible")
    if t < 0:
        t += n

    return t


ai = [int(v) - idx for idx, v in enumerate(data[1].split(",")) if not v == "x"]
Mi = [int(v) for v in data[1].split(",") if not v == "x"]
# ai[0] = 0

print(solve_crt(ai, Mi))
end = time.time()
print("time: ", end-start)
