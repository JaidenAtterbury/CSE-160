# Name: Jaiden Atterbury
# CSE 160
# Homework 6

import utils  # noqa: F401, do not remove if using a Mac
import csv
import random
from operator import itemgetter
import matplotlib.pyplot as plt


# Problem 1:

def extract_election_votes(filename, column_names):
    """Takes a filename and a list of column names and returns a list of
    integers that contains the values in those columns from every row. This
    list will be a list of integers coming from the file.

    Assumptions:
        1.) Since it makes no sense to analyze no data, column_names will never
        be empty.
        2.) Since we are analyzing vote data, the data stored in each row of
        column_names can be converted to an int or is empty.

    Arguments:
        filename: the file that contains the data the user wishes to analyze
        column_names: the columns from the file that the user wants data from

    Returns: a list of integers that contains the values in those columns from
    every row (the order of the integers does not matter).
    """
    # Open the file at filename, then create a csv.DictReader object. For each
    # row that gets turned into a dictionary, use itemgetter to extract the
    # values corresponding to column_names. For each of these values, if the
    # value is not empty remove the comma and turn it into an integer, then
    # append this value to the return list. Lastly, close the file and return
    # the return_list.
    vote_csv = open(filename)
    input_file = csv.DictReader(vote_csv)
    return_list = []
    for row in input_file:
        vote_values = itemgetter(*column_names)(row)
        for value in vote_values:
            if len(value) != 0:
                new_value = int(value.replace(",", ""))
                return_list.append(new_value)
    vote_csv.close()
    return return_list


# Problem 2:

def ones_and_tens_digit_histogram(numbers):
    """Takes a list of integer numbers and produces and returns as output a
    list of 10 numbers. In the returned list, the value at index i is the
    relative frequency with which digit i appeared in the ones place or the
    tens place in the input list. In the input, if a number is less than
    10, such as 1, the tens place is implicitly zero. That is, 1 is treated
    as 01. Your code should treat the tens digits of these values as zero.

    Assumptions:
        1.) Since it makes no sense to analyze no data, numbers will never
        be empty.

    Arguments:
        numbers: a list of integers.

    Returns: a list of 10 numbers with which the value at index i is the
    relative frequency with which digit i appeared in the ones place or the
    tens place in the input list.
    """
    # For each integer in the given list of integers called numbers, extract
    # the number in the tens and/or ones place. With this extracted number,
    # increment the count_list for each digit in the number. Lastly, change
    # this count list into a list of relative frequencies through a list
    # comprehension, then return this list.
    count_list = [0] * 10
    ones_tens_num = 0
    for num in numbers:
        ones_tens_num = num % 100
        if len(str(ones_tens_num)) == 1:
            count_list[0] += 1
        for digit in [int(n) for n in str(ones_tens_num)]:
            count_list[digit] += 1
    rel_freq_list = [num / (2 * len(numbers)) for num in count_list]
    return rel_freq_list


# Problem 3:

def plot_iran_least_digits_histogram(histogram):
    """Takes a histogram as created by ones_and_tens_digit_histogram and
    graphs the frequencies of the ones and tens digits for the Iranian election
    data. Then saves the plot to a file named iran-digits.png using plt.savefig
    The function does not return anything.
    """
    xs = range(10)
    plt.plot(xs, [0.1] * 10, label="ideal")
    plt.plot(xs, histogram, label="iran")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.title("Distribution of the last two digits in Iranian dataset")
    plt.legend(loc='upper left')
    plt.savefig("iran-digits.png")
    # plt.show()
    plt.clf()


# Problem 4:

def int_collection(num_ints):
    """Takes in a a list of integers named num_ints, and creates a list of
    num_ints random numbers. Then the function will create and return a
    relative frequency histogram of these random numbers by calling
    ones_and_tens_histogram.

    Arguments:
        num_ints: a list of integers, denoting the sample size.

    Returns: a list of 10 numbers with which the value at index i is the
    relative frequency with which digit i appeared in the ones place or the
    tens place in the input list. These 10 numbers correspond to the int_list
    that was created in the function.
    """
    # Create num_ints random numbers between 0 and 99 (inclusive) and append
    # them to int_list. Then turn this int_list to a relative frequency list
    # through the use of ones_and_tens_digit_histogram, then return this list.
    int_list = []
    for num in range(num_ints):
        int_list.append(random.randint(0, 99))
    hist_int_list = ones_and_tens_digit_histogram(int_list)
    return hist_int_list


def plot_samples(sample_size):
    """Takes in a a list of integers named sample_size, and creates a list of
    relative frequencies by calling the int_collection function. Then the
    function will plot this data in the form of a line graph.

    Arguments:
        sample_size: a list of integers, denoting the sample size.
    """
    # Given a sample_size, call int_collection to obtain a relative frequency
    # histogram of sample_size integers between [0,99]. Then plot this sample.
    sample = int_collection(sample_size)
    plt.plot(range(0, 10), sample, label=str(sample_size)+" random numbers")


def plot_dist_by_sample_size():
    """Plots line graphs of random integers [0,99] of 5 different sample sizes:
    10, 50, 100, 1000, 10000.
    """
    plt.plot(range(0, 10), [0.1] * 10, label="ideal")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.title("Distribution of the last two digits in randomly generated"
              " samples")
    for size in [10, 50, 100, 1000, 10000]:
        plot_samples(size)
    plt.legend(loc='upper left')
    plt.savefig("random-digits.png")
    plt.show()
    plt.clf()


# Problem 5:

def mean_squared_error(numbers1, numbers2):
    """Takes two lists of numbers, we assume the lists have the same length
    and are not empty. Returns the mean squared error between the lists

    MSE is computed as follows: For each point in one dataset, compute the
    difference between it and the corresponding point in the other dataset.
    Square this difference then take the average of these squared differences.
    """
    # Iterate over the length of numbers1 (could have used numbers2) to obtain
    # the indexes needed for the MSE. At each index, subtract the value of
    # numbers2 from numbers1 then square this value. Add this result to a
    # running total. Once this total is calculated, comopute and return the
    # average.
    total = 0
    for index in range(len(numbers1)):
        total += (numbers1[index] - numbers2[index]) ** 2
    return total / len(numbers1)


# Problem 6:

def calculate_mse_with_uniform(histogram):
    """Takes a histogram as created by ones_and_tens_digit_histogram, then
    Returns the mean squared error of the given histogram with the uniform
    distribution.

    Arguments:
        histogram: a list of relative frequencies.

    Returns: The mean squared error of the given histogram with the uniform
    distribution
    """
    return mean_squared_error(histogram, [0.1] * 10)


# Problem 8

def get_summary(election_string, election_mse, geq_mse, less_mse, p_value):
    """Takes the values calculated and passed in from the compare_to_samples
    function, and prints the expected output from the program.
    """
    print(election_string, "election MSE:", election_mse)
    print("Quantity of MSEs larger than or equal to the", election_string,
          "election MSE:", geq_mse)
    print("Quantity of MSEs smaller than the", election_string,
          "election MSE:", less_mse)
    print(election_string, "election null hypothesis rejection level p:",
          p_value)


def compare_to_samples(election_string, election_mse, num_of_data):
    """Takes three inputs, the Iranian or U.S. MSE as computed by
    calculate_mse_with_uniform and the number of data points in the given
    dataset. The function builds 10,000 groups of random numbers, where each
    number is in between [0, 99], and each group is the same size as the given
    election data. The function then computes the MSE with the uniform
    distribution for each of these groups. Finally, the function compares each
    of these 10,000 MSEs to the election MSE that was passed into the function
    as a parameter.

    Arguments:
        election_string: a string that denotes the year and country analyzed.
        election_mse: the Iranian or U.S. MSE as computed by
                      calculate_mse_with_uniform
        num_of_data: the number of data points in the given dataset.

    Output:
        1.) Determine how many of the random MSEs are larger the election MSE.
        2.) Determine how many of the random MSEs are smaller than the election
            MSE.
        3.) Determine the election null hypothesis rejection level
        4.) Print all of these values after the election MSE.
    """
    # Compute the statistics about the MSE of the given election based on the
    # number of data points in the dataset.
    geq_mse = 0
    less_mse = 0
    for trial in range(1, 10001):
        trial_n_hist = int_collection(num_of_data)
        trial_n_mse = calculate_mse_with_uniform(trial_n_hist)
        if trial_n_mse >= election_mse:
            geq_mse += 1
        else:
            less_mse += 1
    p_value = geq_mse / 10000

    # Compute the output for the elections.
    get_summary(election_string, election_mse, geq_mse, less_mse, p_value)


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    """Takes two inputs, the Iranian MSE as computed by
    calculate_mse_with_uniform and the number of data points in the Iranian
    dataset. The function then calls compare_to_samples which builds 10,000
    groups of random numbers, where each number is in between [0, 99], and
    each group is the same size as the Iranian election data (120 numbers).
    The function then computes the MSE with the uniform distribution for each
    of these groups. Finally, the function compares each of these 10,000 MSEs
    to the Iranian MSE that was passed into the function as a parameter.

    Arguments:
        iran_mse: the Iranian MSE as computed by calculate_mse_with_uniform.
        number_of_iran_datapoints: the number of data points in the Iranian
                                   dataset.

    Output:
        1.) Determine how many of the random MSEs are larger the Iran MSE.
        2.) Determine how many of the random MSEs are smaller than the Iran MSE
        3.) Determine the Iranian election null hypothesis rejection level.
        4.) Print all of these values after the Iranian MSE.
    """
    compare_to_samples("2009 Iranian", iran_mse, number_of_iran_datapoints)


def compare_us_mse_to_samples(us_mse, number_of_us_datapoints):
    """Takes two inputs, the U.S. MSE as computed by calculate_mse_with_uniform
    and the number of data points in the U.S. dataset. The function then calls
    compare_to_samples which builds 10,000 groups of random numbers, where
    each number is in between [0, 99], and each group is the same size as the
    U.S. election data. The function then computes the MSE with the uniform
    distribution for each of these groups. Finally, the function compares each
    of these 10,000 MSEs to the U.S. MSE that was passed into the function as a
    parameter.

    Arguments:
        us_mse: the U.S. MSE as computed by calculate_mse_with_uniform
        number_of_us_datapoints: the number of data points in the U.S. dataset

    Output:
        1.) Determine how many of the random MSEs are larger than the U.S. MSE
        2.) Determine how many of the random MSEs are smaller than the U.S. MSE
        3.) Determine the U.S. election null hypothesis rejection level
        4.) Print all of these values after the U.S. MSE.
    """
    compare_to_samples("2008 United States", us_mse, number_of_us_datapoints)


# The code in this function is executed when this file is run as a Python
# program. The code calls functions you have written above e.g.
# extract_election_vote_counts() etc. This code should produce the output
# expected from your program.
def main():
    # Compute Iran election information
    iran_candidates = ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]
    iran_data = extract_election_votes("election-iran-2009.csv",
                                       iran_candidates)
    iran_hist = ones_and_tens_digit_histogram(iran_data)
    iran_mse = calculate_mse_with_uniform(iran_hist)

    # Compute United States election information
    us_candidates = ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]
    us_data = extract_election_votes("election-us-2008.csv", us_candidates)
    us_hist = ones_and_tens_digit_histogram(us_data)
    us_mse = calculate_mse_with_uniform(us_hist)

    # Plot Iran election information and random samples
    plot_iran_least_digits_histogram(iran_hist)
    plot_dist_by_sample_size()

    # Compute expected output
    compare_iran_mse_to_samples(iran_mse, len(iran_data))
    print()
    compare_us_mse_to_samples(us_mse, len(us_data))


if __name__ == "__main__":
    main()
