# ############################################
# # PART 1
# ############################################
 
with open("07/input.txt") as file:
    data = file.read().split(",")

crab_positions = [int(i) for i in data]

best_destination = 0
best_fuel_cost = float('inf')

for destination in range(min(crab_positions), max(crab_positions)):
    fuel_cost = sum(abs(current_position - destination) for current_position in crab_positions)
    if fuel_cost < best_fuel_cost:
        best_fuel_cost = fuel_cost
        best_destination = destination

red = "\033[1m\033[38;5;1m" #\033[1m makes it bold. \033[38;5;1m makes it red. 
reset = "\033[0m"
print(f"""
┌── {red}(\)_( ╯ ─ ╯)_(/){reset} ── Part 1 ── {red}(\)_(╰ ─ ╰)_(/){reset} ──┐

   Best destination for the crabs:      {best_destination}
   Fuel cost of destination {best_destination}:        {best_fuel_cost}

└── {red}(\)_( ╯ ─ ╯)_(/){reset} ──────────── {red}(\)_(╰ ─ ╰)_(/){reset} ──┘
""")

############################################
# PART 2
############################################

def get_cost(x1, x2): # get cost to travel between two x_positions
    distance = abs(x1 - x2)
    return distance*(distance+1)//2 # equation for triangle number sequence

with open("07/input.txt") as file:
    data = file.read().split(",")

crab_positions = [int(i) for i in data]

best_destination = 0
best_fuel_cost = float('inf')

for destination in range(min(crab_positions), max(crab_positions)):
    fuel_cost = sum(get_cost(current_position, destination) for current_position in crab_positions)  # the only change from part 1 to part 2 is this new `get_cost` function
    if fuel_cost < best_fuel_cost:
        best_fuel_cost = fuel_cost
        best_destination = destination

red = "\033[1m\033[38;5;1m" #\033[1m makes it bold. \033[38;5;1m makes it red. 
reset = "\033[0m"
print(f"""
┌── {red}(\)_( ╯ ─ ╯)_(/){reset} ── Part 2 ── {red}(\)_(╰ ─ ╰)_(/){reset} ──┐

   Best destination for the crabs:      {best_destination}
   Fuel cost of destination {best_destination}:        {best_fuel_cost}

└── {red}(\)_( ╯ ─ ╯)_(/){reset} ──────────── {red}(\)_(╰ ─ ╰)_(/){reset} ──┘
""")