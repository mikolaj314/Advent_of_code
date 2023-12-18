from collections import defaultdict
with open('input.txt') as file:
    text = file.read().strip()
    lines = text.split('\n')

grid = [[c for c in line] for line in lines]
R = len(grid)
C = len(grid[0])

result1 = 0
result2 = 0
has_symbol = False
nums = defaultdict(list)
for row in range(R):
    n = 0
    gears = set()
    for column in range(C + 1):
        if column < C and grid[row][column].isdigit():
            n = n * 10 + int(grid[row][column])
            for row_vector in [-1, 0, 1]:
                for column_vector in [-1, 0, 1]:
                    if 0 <= row + row_vector < R and 0 <= column + column_vector < C:
                        char = grid[row + row_vector][column + column_vector]
                        if char != '.' and not char.isdigit():
                            has_symbol = True
                        if char == '*':
                            gears.add((row + row_vector, column + column_vector))
        elif n > 0:
            if has_symbol:
                result1 += n

            for gear in gears:
                nums[gear].append(n)

            n = 0
            has_symbol = False
            gears = set()

for gear, numbers in nums.items():
    if len(nums[gear]) == 2:
        result2 += numbers[0] * numbers[1]

print(result1)
print(result2)
