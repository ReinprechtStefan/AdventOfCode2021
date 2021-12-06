def map_list(str_list):
    #print(str_list)
    return list(map(lambda val : Board_Position(int(val)), str_list))

class Board_Position:
    selected = False

    def __init__(self, value):
        self.value = value

class Board:
    def __init__(self, line0, line1, line2, line3, line4):
        self.board_positions = []
        self.board_positions.append(map_list(str(line0).split(" ")))
        self.board_positions.append(map_list(str(line1).split(" ")))
        self.board_positions.append(map_list(str(line2).split(" ")))
        self.board_positions.append(map_list(str(line3).split(" ")))
        self.board_positions.append(map_list(str(line4).split(" ")))
        
    def check_bingo(self, number):
        if number == 16:
            print("jff")
        for row in self.board_positions:
            for num in row:
                if num.value == number:
                    num.selected = True

        for row in self.board_positions:
            if row[0].selected and row[1].selected and row[2].selected and row[3].selected and row[4].selected:
                return True

        for i in range(5):
            if self.board_positions[0][i].selected and self.board_positions[1][i].selected and self.board_positions[2][i].selected and self.board_positions[3][i].selected and self.board_positions[4][i].selected:
                return True

        return False
    
    def calc_unselected_val(self):
        val = 0
        i = 0
        for row in self.board_positions:
            for num in row:
                i += 1
                if num.selected == False:
                    val += num.value
        return val


def get_bingo_numbers(line):
    return list(map(int, str(line).split(",")))


def get_bingo_boards(lines):
    boards = []

    line0 = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for line in lines:
        if line == "\n":
            b = Board(line0, line1, line2, line3, line4)
            boards.append(b)
            line0 = ""
            line1 = ""
            line2 = ""
            line3 = ""
            line4 = ""

        if line0 == "":
            line0 = str(line).strip().replace("  ", " ")
        elif line1 == "":
            line1 = str(line).strip().replace("  ", " ")
        elif line2 == "":
            line2 = str(line).strip().replace("  ", " ")
        elif line3 == "":
            line3 = str(line).strip().replace("  ", " ")
        elif line4 == "":
            line4 = str(line).strip().replace("  ", " ")

    boards.append(Board(line0, line1, line2, line3, line4))

    return boards


with open('input.txt') as f:
    lines = f.readlines()

    bingo_numbers = get_bingo_numbers(lines[0])

    boards = get_bingo_boards(lines[2:])
    solved_boards = []

    score = 0
    bingo_number = 0
    for number in bingo_numbers:
        print(number)
        for board in boards:
            if board in solved_boards:
                continue
            if board.check_bingo(number):
                print("bingo", number)
                solved_boards.append(board)

            if len(solved_boards) == len(boards):
                score = board.calc_unselected_val()
                #print(number)
                bingo_number = number
                break
        if score != 0:
            break
    
    print(score * bingo_number)