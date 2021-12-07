############################################
# PART 1
############################################

FORMATTING_FILLED_SPACE = "\033[38;5;154m" # 38 means foreground; 5; 154 means yellow
FORMATTING_RESET = "\033[0m" # reset
FORMATTING_WINNING_SPACE = "\033[48;5;022m" # 48 means background; 5; 022 means forest green

class Board:
    board_id = 0
    winning_line = -1
    winning_col = -1

    def __init__(self, board_text):
        self.board_id = Board.board_id
        Board.board_id += 1

        self.numbers = []
        self.spots_marked = [[False]*5 for i in range(5)]

        lines = board_text.splitlines()
        for i, line in enumerate(lines):
            self.numbers.append([int(num) for num in line.split()])

    def __str__(self) -> str:
        _str =  "╔══════════════════════╗\n"
        _str += "╟── BINGO BOARD: {:03} ──╢\n".format(self.board_id) # format board ID two be 3 characters long, with leading zeros if needed
        for x in range(5):
            _str += "║ "
            for y in range(5):    
                # color the next number
                if x == self.winning_line or y == self.winning_col:
                    _str += FORMATTING_RESET + FORMATTING_WINNING_SPACE
                elif self.spots_marked[x][y]:
                    _str += FORMATTING_FILLED_SPACE
                # print the next number
                _str += f"{self.numbers[x][y]:3} " # format number ID two be 3 characters long, with leading spaces  if needed
                _str += FORMATTING_RESET
            _str += " ║\n"
        _str += "╚══════════════════════╝"
        return _str
    
    def sum_of_all_unmarked_numbers():
        pass

    def draw_number(self, new_number): # returns whether this board just won
        has_number = False
        for x, line in enumerate(self.numbers):
            for y, number in enumerate(line):   
                if (new_number == number):
                    has_number = True
                    self.spots_marked[x][y] = True
                    # check for bingo:
                    # horizontal bingo
                    won = False
                    if all(self.spots_marked[x][col] for col in range(5)):
                        self.winning_line = x
                        won = True
                    # vertical bingo
                    if all(self.spots_marked[row][y] for row in range(5)):
                        self.winning_col = y
                        won = True
                    if (won):
                        return True
        return False
    
    def get_score(self):
        score = 0
        for x in range(5):
            for y in range(5):
                marked = self.spots_marked[x][y]
                num = self.numbers[x][y]
                if not marked:
                    score += num
        return score

############################################
# PART 1
############################################

def part_1():
    with open("04\input_1.txt") as file:
        numbers_drawn = next(file)
        next(file) # get rid of the first empty line before the boards start
        data = file.read().split("\n\n")
        boards = [Board(b) for b in data]

        for number in numbers_drawn.split(","):
            number = int(number)
            for i, board in enumerate(boards):
                if board.draw_number(number): # if this number won
                    print()
                    print("~~~~~~~~~~~~~~ Part 1 ~~~~~~~~~~~~~~")
                    print("Winning board:")
                    print(board)
                    print(f"Winning score: {board.get_score()}")
                    print(f"Winning number: {number}")
                    print(f"Result: {board.get_score() * number}")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    return

part_1()

############################################
# PART 2
############################################

def part_2():
    Board.board_id = 0 # reset board IDs (just so the displays look nice)
    with open("04\input_1.txt") as file:
        numbers_drawn = next(file)
        next(file) # get rid of the first empty line before the boards start
        data = file.read().split("\n\n")
        boards = [Board(b) for b in data]

        board = None
        numbers = numbers_drawn.split(",")
        last_number_drawn_index = 0
        for i in range(len(numbers)):
            number = int(numbers[i])
            boards = [b for b in boards if not b.draw_number(number)] # keep all boards that didn't get bingo
            if len(boards) == 1: # we've found the last board to get bingo
                board = boards[0]
                last_number_drawn_index = i
                break
        for i in range(last_number_drawn_index, len(numbers)):
            number = int(numbers[i])
            if board.draw_number(number): # if this number won
                print()
                print("~~~~~~~~~~~~~~ Part 2 ~~~~~~~~~~~~~~")
                print("Last board to win bingo:")
                print(board)
                print(f"Winning score: {board.get_score()}")
                print(f"Winning number: {number}")
                print(f"Result: {board.get_score() * number}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break
        
part_2()
