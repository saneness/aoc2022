from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=20)
data = list(map(int, puzzle.input_data.splitlines()))

def make_unique(numbers, decryption_key=1):
    numbers = numbers.copy()
    count = {}
    for i in range(len(numbers)):
        if numbers[i] in count:
            count[numbers[i]] += 1
        else:
            count[numbers[i]] = 0
        numbers[i] = numbers[i] * 10 * decryption_key + count[numbers[i]]
    return numbers

def mix(numbers, times):
    initial = numbers.copy()
    numbers = numbers.copy()
    for _ in range(times):
        for i, number in enumerate(initial):
            if number != 0:
                j = numbers.index(number)
                numbers.insert((j + number // 10) % (len(numbers) - 1), numbers.pop(j))
                if j + number // 10 == 0:
                    numbers = numbers[1:] + [numbers[0]]
    return numbers

unmake_unique = lambda x: [i // 10 for i in x]

numbers = make_unique(data)
after_first = unmake_unique(mix(numbers=numbers, times=1))

numbers = make_unique(numbers=data, decryption_key=811589153)
numbers = unmake_unique(mix(numbers=numbers, times=10))

groove_coordinates = lambda x: sum([x[(x.index(0) + i) % len(x)] for i in [1000, 2000, 3000]])

answer_a = groove_coordinates(after_first)
answer_b = groove_coordinates(numbers)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b