# Name: Jaiden Atterbury
# CSE 160
# Autumn 2022
# Midterm Exam


# Problem 1
def find_days(dates_list):
    """
    Returns the average day of all dates in the list dates_list.

    Arguments:
        dates_list (list): a list of date strings in the form "mm/dd/yy".

    Return:
        The average of all days in dates_list as an integer, where any
        fractional portion has been dropped.
    """
    day_total = 0
    for date in dates_list:
        # If the day is 01-09, only take the positive digit
        if int(date[3]) == 0:
            int_day = int(date[4])
        # If the day is 10-31, take both digits
        else:
            int_day = int(date[3:5])
        day_total += int_day
    return day_total // len(dates_list)


assert find_days(["12/12/12", "02/02/12", "05/10/13"]) == 8
assert find_days(["03/08/92", "11/01/19"]) == 4
assert find_days(["06/16/13", "06/16/13"]) == 16


# Problem 2
def plan_trip(weather, temps):
    """
    Given two lists weather and temps, return the day number where the weather
    is clear and the temperature is maximum, along with the temperature on
    that day. The day number is the position in either list (counting from 1).

    Arguments:
        weather (list): List of weather forecasts for the next few days.
        temps (list): List of temperatures for the next few days. All
        temperatures will be unique.

    Returns:
        a list with the day number and the temperature for that day
        in the format: [day_number, temperature_on_the_day]
        Returns the string "No Clear Weather!" if no clear day is forecast.
        Returns the string "Missing Data!" if either of the lists is empty.
    """
    # Check to make sure weather or temps aren't empty
    if len(weather) == 0 or len(temps) == 0:
        return "Missing Data!"
    # Check to see if there are any clear days in the forecast
    if "clear" not in weather:
        return "No Clear Weather!"

    max_day = 0
    max_temp = 0
    # Find the maximum temperature and which day it occurs on
    for index in range(len(weather)):
        if weather[index] == "clear" and temps[index] > max_temp:
            max_temp = temps[index]
            max_day = index + 1
    return [max_day, max_temp]


assert plan_trip(["sunny", "rainy", "clear", "clear"],
                 [39, 37, 22, 30]) == [4, 30]
assert plan_trip(["clear", "sunny", "rainy"], []) == "Missing Data!"
assert plan_trip(["sunny", "rainy", "rainy", "sunny"],
                 [39, 37, 22, 30]) == "No Clear Weather!"


# Problem 3
def recommend_restaurant(restaurants, min_rating):
    """
    Finds all restaurants with a rating greater than or equal to min_rating.

    Arguments:
        restaurants (list): A list of [restaurant, rating] pairs
        min_rating (number): The minimum rating a restaurant can have to be
        considered for dinner

    Returns:
        a sorted list of restaurant names with ratings greater
        than or equal to min_rating
    """
    accepted_list = []
    for place in restaurants:
        if place[1] >= min_rating:
            accepted_list.append(place[0])
    accepted_list.sort()
    return accepted_list


assert recommend_restaurant([["shawarma king", 4.4],
                             ["cedars", 4.2],
                             ["chipotle", 3.6],
                             ["nuodle express", 2.9]], 3.6) ==\
                            ["cedars", "chipotle", "shawarma king"]
assert recommend_restaurant([], 5) == []
assert recommend_restaurant([["cedars", 4.2],
                             ["shawarma king", 4.4],
                             ["chipotle", 3.6],
                             ["nuodle express", 2.9]], 5) == []


# Problem 4
def zombie_list(initial_list, output_list_size, bunch_size):
    """
    Returns a new list based on initial_list.

    Arguments:
        initial_list (list): a list of ints that the returned list is based on
        output_list_size (int): the number of ints in the returned list
        bunch_size (int): the number of previous values in the list that should
        be summed to create the next entry in the returned list

    Returns:
        A list of output_list_size ints created from intitial_list by summing
        the prior bunch_size values to create the next entry.
    """
    new_list = initial_list[:]
    for i in range(len(new_list), output_list_size):
        total = 0
        for j in range(-1 * bunch_size, 0):
            total += new_list[j]
        new_list.append(total)
    return new_list


assert zombie_list([1, 2, 3], 6, 2) == [1, 2, 3, 5, 8, 13]
assert zombie_list([4, 1, -2, 3], 9, 3) == [4, 1, -2, 3, 2, 3, 8, 13, 24]
assert zombie_list([0, -4, -2], 10, 1) ==\
                   [0, -4, -2, -2, -2, -2, -2, -2, -2, -2]


# Problem 5
def plot_flowers(placements, num_rows, num_cols):
    """
    Generates and returns a num_rows x num_cols grid as a lists of lists
    representation of the garden, with flowers represented as 1. Locations in
    the grid with no flowers should be marked with 0.

    Arguments:
        placements (list): a list of lists, where each item represents
        the [row, col] placement of a flower. The [row, col] items are unique.
        num_rows (int): the number of rows in the garden
        num_cols (int): the number of columns in the garden

    Returns:
        a num_rows x num_cols grid in a list of lists format representing
        the garden.
    """
    # Create "template" of the garden grid
    flower_grid = []
    for row in range(num_rows):
        temp_row = []
        for col in range(num_cols):
            temp_row.append(0)
        flower_grid.append(temp_row)
    # Add the flowers (1's) to the grid
    for i, j in placements:
        flower_grid[i][j] = 1
    return flower_grid


assert plot_flowers([[1, 2], [0, 3], [2, 1], [0, 2]], 3, 4) ==\
     [[0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 0, 0]]
assert plot_flowers([], 3, 2) == [[0, 0], [0, 0], [0, 0]]
assert plot_flowers([[0, 0]], 1, 1) == [[1]]


# ANSWER the following questions as COMMENTS

# (1 pt) Did you work on this quiz alone or collaborate with others?

# If you collaborated with others, list full names and UWNetIDs
# of everyone you collaborated with.

# Yes, on this quiz I briefly collaborated with Tanner Huck (thuck).
