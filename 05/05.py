def lerp(a, b, t, length):
    return (t * a + (length-t) * b)//length
    
data = None

with open("05/input.txt") as file:
    data = file.read().splitlines()

ONE_VENT = 1
TWO_OR_MORE_VENTS = 2

def count_danger_zones(should_consider_diagonals):
    map = {}
    danger_zones = 0
    for line in data:
        coords1, coords2 = line.split(" -> ")
        x1, y1 = [int(c) for c in coords1.split(",")]
        x2, y2 = [int(c) for c in coords2.split(",")]
        if x2-x1 != 0 and y2 - y1 != 0 and not should_consider_diagonals:
            continue
        dist = max(abs(y2-y1), abs(x2-x1))
        for i in range(dist+1):
            x = lerp(x2, x1, i, abs(x2 - x1) if x1 != x2 else 1)
            y = lerp(y2, y1, i, abs(y2 - y1) if y1 != y2 else 1)
            if not x in map:
                map[x]= {}
            if not y in map[x]:
                map[x][y] = ONE_VENT
            elif map[x][y] == ONE_VENT:
                map[x][y] = TWO_OR_MORE_VENTS
                danger_zones += 1
            else: # map[x][y] has two or more vents already
                continue
    return danger_zones

print(">──────── Part 1 ────────<")
print("(Only consider horizontal and vertical vents.)")
print(f"Number of danger zones: {count_danger_zones(should_consider_diagonals=False)}")
print(">────────────────────────<")
print()
print(">──────── Part 2 ────────<")
print("(Also consider diagonal vents.)")
print(f"Number of danger zones: {count_danger_zones(should_consider_diagonals=True)}")
print(">────────────────────────<")