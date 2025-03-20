import numpy as np

# Basic exercises around matrices.
# Try to implement (code) the behaviour described in each function
# You do not need to modify the signature (declarations) of any function, but experiment if you want

def generate_random_matrix(rows: int, columns: int) -> np.matrix[int]:
    # Generate and return a matrix filled with random int between 1 and 100
    # Yhe matrix must be of the size specified by the parameters (rows, columns)
    # Hint: you might need to import a library. Google and Chatgpt are your friends

    return None # change this line to return the matrix


def get_biggest_element(matrix: np.matrix[int]) -> int:
    # Takes a matrix of int (integers) and returns the biggest integer in that matrix
    # Do not modify the input matrix
    # This function should work with matrices of any size

    return None # change this line to return the number

def sum_by_collumns(matrix: np.matrix[int]) -> list[int]:
    # Takes a matrix of int (integers) and obtains the sum of the numbers of each collumn
    # For example, if i input the matrix:
    # | 1   3   10 |
    # | 5   2   5  |
    # I would expect the output to be a list:
    # [ 6   5   15 ]
    #
    # As allways, do not modify the matrix and you algorithm must work for any size of matrices

    return None # change this line to return the list

if __name__ == "__main__":
    random_matrix = generate_random_matrix(10, 5)
    print(f"Generated {random_matrix}")
    biggest_element = get_biggest_element(random_matrix)
    print(f"Its biggets element is {biggest_element}")
    sums = sum_by_collumns(random_matrix)
    print(f"Its columns sums are {sums}")