assingment 1 random magic squares 
author ahmad siyar 
subject ICS4U0-1

import random
import numpy as np

def is_prime(n):
    """ Check if a number is prime """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_matrix_1(n):
    """ Generate the first matrix with random permutation of 1 to N """
    numbers = list(range(1, n + 1))
    random.shuffle(numbers)
    matrix = []
    for i in range(n):
        if i == 0:
            matrix.append(numbers)
        else:
            # Shift last two numbers to the front
            next_row = matrix[i - 1][-2:] + matrix[i - 1][:-2]
            matrix.append(next_row)
    return matrix

def generate_matrix_2(n):
    """ Generate the second matrix with random permutation of multiples of N """
    numbers = [i * n for i in range(n)]
    random.shuffle(numbers)
    matrix = []
    for i in range(n):
        if i == 0:
            matrix.append(numbers)
        else:
            # Shift last three numbers to the front
            next_row = matrix[i - 1][-3:] + matrix[i - 1][:-3]
            matrix.append(next_row)
    return matrix

def is_magic_square(square):
    """ Check if the square is a magic square """
    n = len(square)
    magic_sum = sum(square[0])
    
    # Check rows and columns
    for i in range(n):
        if sum(square[i]) != magic_sum or sum(row[i] for row in square) != magic_sum:
            return False
    
    # Check diagonals
    if sum(square[i][i] for i in range(n)) != magic_sum:
        return False
    if sum(square[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False
    
    return True

def magic_sum(n):
    """ Calculate the magic sum for an N x N magic square """
    return n * (n**2 + 1) // 2

def main():
    # Input
    N = int(input("Enter a prime number N between 5 and 19: "))
    
    # Validate input
    if N < 5 or N > 19 or not is_prime(N):
        print("Invalid input. Please enter a prime number between 5 and 19.")
        return
    
    # Generate matrices
    matrix_1 = generate_matrix_1(N)
    matrix_2 = generate_matrix_2(N)
    
    # Create magic square by adding both matrices
    magic_square = np.add(matrix_1, matrix_2).tolist()
    
    # Calculate magic sum
    magic_sum_value = magic_sum(N)
    
    # Check if the result is a magic square
    magic_check = is_magic_square(magic_square)
    
    # Output
    print("Magic Square:")
    for row in magic_square:
        print(row)
    print(f"Magic Sum: {magic_sum_value}")
    print("Is the square magic? " + ("Yes" if magic_check else "No"))

if __name__ == "__main__":
    main()
