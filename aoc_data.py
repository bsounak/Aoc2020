import os

cache = os.path.join(os.path.expanduser("~"), ".aoc2020")

def load(day):
    if not os.path.exists(cache):
        os.makedirs(cache)

    fname = "day" + str(int(day)) + ".txt"
    if not os.path.isfile(os.path.join(cache, fname)):
        raise Exception(
            "No data available for day{} at {}".format(day, cache)
        )
    with open(os.path.join(cache, "day1.txt"), "rb") as f:
        data = f.read()
        data = [int(v) for v in data.split()]

    return data
