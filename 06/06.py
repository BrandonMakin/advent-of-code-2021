############################################
# PART 1
############################################

# data = None

# with open("06/test.txt") as file:
#     data = [int(i) for i in file.read().split(",")]

# expected = []
# days = 18
# for i in range(days):
#     data = [6 if fish == 0 else fish-1 for fish in data] + [8 for fish in data if fish == 0]
# print(len(data))

############################################
# PART 2
############################################

# --------------- debug code ---------------
arrow_0 = " ^  1  2  3  4  5  6 "
def debug_print_fish_counts(i):
    print("------------------------")
    print(f"Day {i:>4}:",fishes, babies)
    global arrow_0
    arrow_0_colored = "          " + "\033[38;5;154m" + arrow_0 + "\033[38;5;156m" + "  7  8" + "\033[0m"
    arrow_0 = arrow_0[-3:] + arrow_0[:-3]
    print(arrow_0_colored)

# --------------- actual important stuff for part 2 ---------------
with open("06/test.txt") as file:
    data = file.read().split(",")

fishes = [0] * 7 # fish with timers 0-6
babies = [0] * 2 # fish with timers 7 and 8. babies[0] is fish at time = 7 days. babies[1] is 8 days
timer_index = 0
days = 256

# put initial fishies in `fishes` array
for f in data:
    fishes[int(f)] += 1

for i in range(days):
    index_for_time_0 = i % 7
    new_fishes = fishes[index_for_time_0]
    fishes[index_for_time_0] += babies[0] # add fish from 7 days to 6 days (actually add them to 0 days, because they'll be 6 days next round)
    babies[0] = babies[1] # move fish from 8 days to 7 days
    babies[1] = new_fishes # get new fish
    # debug_print_fish_counts(i)
print(sum(fishes) + sum(babies))