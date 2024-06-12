# Name: Jaiden Atterbury
# CSE 160
# Homework 6

import fraud_detection as fd
import math

# Helper function for test_ones_and_tens_digit_histogram


def one_ten_helper(actual, expected):
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])

# Given test function


def test_ones_and_tens_digit_histogram():
    # example from spec
    one_ten_helper(fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90]),
                   [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2])

    # test case 2: all zeros
    one_ten_helper(fd.ones_and_tens_digit_histogram([0, 0, 0, 0, 0]),
                   [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # test case 3: length 1
    one_ten_helper(fd.ones_and_tens_digit_histogram([127]),
                   [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0])

    # test case 4: all single digit
    one_ten_helper(fd.ones_and_tens_digit_histogram([1, 2, 3, 4, 5]),
                   [0.5, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0])

    # test case 5: all not single digit
    one_ten_helper(fd.ones_and_tens_digit_histogram([10, 24, 13, 124, 15]),
                   [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0])

    print("passed test_ones_and_tens_digit_histogram!")


# implemented test function #1


def test_mean_squared_error():
    # example from spec
    assert math.isclose(17.0, fd.mean_squared_error([1, 4, 9], [6, 5, 4]))

    # one point
    assert math.isclose(1.0, fd.mean_squared_error([1], [2]))

    # same line
    assert math.isclose(0.0, fd.mean_squared_error([1, 4, 9], [1, 4, 9]))

    # all zeros
    assert math.isclose(0.0, fd.mean_squared_error([0, 0, 0], [0, 0, 0]))

    print("passed test_mean_squared_error!")


# implemented test function #2


def test_calculate_mse_with_uniform():
    uniform = [0.1] * 10

    # example from spec
    test_list_1 = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    assert math.isclose(0.01, fd.calculate_mse_with_uniform(test_list_1))

    # same histogram
    assert math.isclose(0.0, fd.calculate_mse_with_uniform(uniform))

    # only 1.0 and 0.0 frequencies
    test_list_2 = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert math.isclose(0.09, fd.calculate_mse_with_uniform(test_list_2))

    print("passed test_calculate_mse_with_uniform!")


def main():
    test_ones_and_tens_digit_histogram()
    test_mean_squared_error()
    test_calculate_mse_with_uniform()


if __name__ == "__main__":
    main()
