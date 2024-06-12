# Name: Jaiden Atterbury
# CSE 160
# Autumn 2022
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and then copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all of the problems given.

# Uncomment the line below to make the math.sqrt function available
import math

# Problem 1
print("Problem 1 solution follows:")

# The goal of this simple program is to compute and print the roots
# of the quadratic equation 3x^2-5.86x+2.5408.

# Start by storing the a,b and c values of the quadratic into variables
# following the ax^2+bx+c conventions of a quadratic polynomial:
a = 3
b = -5.86
c = 2.5408

# Compute the roots of the quadratic using the quadratic formula:
small_root = ((-1 * b) - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
large_root = ((-1 * b) + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

# Print the results, with the smaller root presented first:
print("Root 1:", small_root)
print("Root 2:", large_root)
print()

# Problem 2
print("Problem 2 solution follows:")

# This small program uses a for loop to print out the decimal versions of
# 1/2, 1/3, ..., 1/10.

for i in range(2, 11):
    print("1/" + str(i) + ":", 1 / i)
print()

# Problem 3
print("Problem 3 solution follows:")

# This simple program will use a for loop and a formula to compute
# the 10th triangular number.

n = 10
triangular = 0

# Create for loop to calculate 10th triangular number:
for i in range(1, n + 1):
    triangular = i + triangular
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n * (n + 1) / 2)
print()

# Problem 4
print("Problem 4 solution follows:")

# This simple program will use a for loop to compute and print the
# 10th factorial.

n = 10
factorial = 1

# Create a for loop to calculate the 10th factorial:
for i in range(2, n + 1):
    factorial = factorial * i
print(str(n) + "!:", factorial)
print()

# Problem 5
print("Problem 5 solution follows:")

# This simple program will use a nested for loop to compute and
# print the 10th factorial all the way down to the 1st factorial
# in descending order.

num_lines = 10

# Outer loop will set the variable n to the value of the nth
# factorial in descending order. It will also print the results
# of the loop:
for i in range(0, num_lines):
    n = num_lines - i
    factorial = 1

    # Inner loop will compute the factorial:
    for j in range(1, n + 1):
        factorial = factorial * j
    print(str(n) + "!:", factorial)
print()

# Problem 6
print("Problem 6 solution follows:")

# This simple program will use a single for loop to approximate
# the number e through the use of adding 1 + 1/1! + 1/2! + ... + 1/10!

n = 10
factorial = 1
total = 1

# Create a for loop to repeatedly compute factorials and add their
# reciprocal to a total_factorial variable
for j in range(1, n + 1):
    factorial = factorial * j
    recp_factorial = 1 / factorial
    total = total + recp_factorial
print("e:", total)

# Collaboration

# For this assignment, I didn't collaborate with anyone.
