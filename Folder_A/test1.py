# this is a new function that is used to test code standards.
def my_function():
    """Do nothing, but document it.No, really, it doesn't do anything."""
    pass


squares = [x**2 for x in range(10)]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)
