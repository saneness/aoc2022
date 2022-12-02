from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=2)
data = [item.split(' ') for item in puzzle.input_data.splitlines()]

game_score = {
    'A': {'X': 4, 'Y': 8, 'Z': 3},
    'B': {'X': 1, 'Y': 5, 'Z': 9},
    'C': {'X': 7, 'Y': 2, 'Z': 6},
    'X': {'A': 3, 'B': 1, 'C': 2},
    'Y': {'A': 4, 'B': 5, 'C': 6},
    'Z': {'A': 8, 'B': 9, 'C': 7}
}

def score(games):
    result = 0
    for game in games:
        result += game_score[game[0]][game[1]]
    return result

answer_a = score(data)
answer_b = score([item[::-1] for item in data])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b