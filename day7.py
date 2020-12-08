import time
import aoc_data

data = aoc_data.load(7).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]

start = time.time()
bdict = {}
for line in data:
    bag, contains = line.split("contain")
    bag = "".join(bag.split("bags")).strip()
    contains = [v.strip() for v in contains.split(",")]
    bdict[bag] = contains


def can_contain(bag1, bag2):
    """
    Return True if bag1 can contain bag2, False otherwise.
    """
    if bag2 in "".join(bdict[bag1]):
        return True

    flags = []
    for item in bdict[bag1]:
        if not "no other bag" in item:
            flags.append(can_contain(" ".join(item.split()[1:3]), bag2))
    return any(flags)


print(sum([can_contain(bag, "shiny gold") for bag in bdict.keys()]))


def contains(bag):
    """
    Return the number of bags a bag can contain
    """
    if "no other bag" in "".join(bdict[bag]):
        return 0

    s = 0
    for item in bdict[bag]:
        s += int(item.split()[0])
        s += int(item.split()[0]) * contains(" ".join(item.split()[1:3]))
    return s


print(contains("shiny gold"))
