# Special Features

## List Comprehension

nums = range(10)
print(nums)

squares = [x*x for x in nums]
print(squares)

squares_over_10 = [x for x in squares if x > 10]
print(squares_over_10)

sum_of_squares = sum(squares_over_10)
print(sum_of_squares)

## Generators

def generate_indices_in_matrix(n, m):
    for i in range(n):
        for j in range(m):
            yield i, j

for i, j in generate_indices_in_matrix(3, 3):
    print(i, j, end=', ')