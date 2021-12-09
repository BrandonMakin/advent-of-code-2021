############################################
# PART 1
############################################
with open("08/test.txt") as file:
    data = file.read().splitlines()

unique_lengths = [2, 3, 4, 7, 8]
output = [line.split(" | ")[1] for line in data]
answers = sum([len([word for word in words.split() if len(word) in unique_lengths]) for words in output])
print(answers)

############################################
# PART 2
############################################
