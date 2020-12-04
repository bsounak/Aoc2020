import re
import time
import aoc_data

start = time.time()

data = aoc_data.load(4).rstrip(b"\n").split(b"\n\n")
data = [v.decode("utf-8").split() for v in data]

passport = []
for i in data:
    pdict = {}
    for j in i:
        key, val = j.split(":")
        pdict[key] = val
    passport.append(pdict)
mandatory_fields = set(["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"])
optional_fields = set(["cid"])

def valid_height(height):
    if height.endswith("cm") and len(height) == 5:
        if height[0].isdigit and height[1].isdigit and height[2].isdigit:
            if 150 <= int(height[:3]) <= 193:
                return True
    if height.endswith("in") and len(height) == 4:
        if height[0].isdigit and height[1].isdigit:
            if 59 <= int(height[:2]) <= 76:
                return True
    return False

nvalid = 0
for p in passport:
    try:
        if not mandatory_fields.issubset(set(p.keys())):
            raise ValueError

        if not len(p["byr"]) == 4:
            raise ValueError
        if not 1920 <= int(p["byr"]) <= 2002:
            raise ValueError

        if not len(p["iyr"]) == 4:
            raise ValueError
        if not 2010 <= int(p["iyr"]) <= 2020:
            raise ValueError

        if not len(p["eyr"]) == 4:
            raise ValueError
        if not 2020 <= int(p["eyr"]) <= 2030:
            raise ValueError

        if not valid_height(p["hgt"]):
            raise ValueError

        if not re.match(r"#[a-f0-9]{6}", p["hcl"]):
            raise ValueError

        if not p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            raise ValueError

        if not len(p["pid"]) == 9:
            raise ValueError
        if not all([s.isdigit() for s in p["pid"]]):
            raise ValueError
    except ValueError:
        pass
    else:
        nvalid += 1

print(nvalid)

end = time.time()
print("time: ", end-start)
