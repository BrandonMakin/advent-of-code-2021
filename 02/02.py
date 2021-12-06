############################################
# PART 1
############################################

with open("02\input_1.txt") as file:
    data = file.read().splitlines()

    horizontal_position = 0
    depth = 0

    for d in data:
        direction, distance = d.split(" ") # split "forward 6" to "forward", "6"
        distance = int(distance)

        match direction:
            case "forward":
                horizontal_position += distance
            case "down":
                depth += distance
            case "up":
                depth -= distance
    print(f"""
■────────── PART 1 ──────────■
  Horizontal position: {horizontal_position}
  Depth: {depth}
  Part 1 answer: {horizontal_position * depth}
■────────────────────────────■
""")

############################################
# PART 2
############################################

with open("02\input_2.txt") as file:
    data = file.read().splitlines()

    horizontal_position = 0
    depth = 0
    aim = 0

    for d in data:
        direction, distance = d.split(" ") # split "forward 6" to "forward", "6"
        distance = int(distance)

        match direction:
            case "forward":
                horizontal_position += distance
                depth += distance * aim
            case "down":
                aim += distance
            case "up":
                aim -= distance

    print(f"""
■────────── PART 2 ──────────■
  Aim: {aim}
  Horizontal position: {horizontal_position}
  Depth: {depth}
  Part 2 answer: {horizontal_position * depth}
■────────────────────────────■
""")