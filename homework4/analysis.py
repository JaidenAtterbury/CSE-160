# Name: Jaiden Atterbury
# CSE 160
# Homework 4


from kmeans import get_closest_centroid
from utils import load_centroids, read_data, assert_equals


# ----------------------------------------------------------
# PROBLEMS FOR STUDENTS


def update_assignment(list_of_points, labels, centroids_dict):
    """Assign all data points to the closest centroids and keep track of their
    labels. The i-th point in "data" corresponds to the i-th label in "labels".

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of ints representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are a list of labels of the data points that are assigned
             to that centroid.

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            labels = [2, 1, 3]
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                              "centroid2": [2, 2, 2, 2]}
            print(update_assignment(list_of_points, labels, centroids_dict))
        Output:
            {'centroid1': [2, 3], 'centroid2': [1]}
    """

    # For each point, find the closest centroid. If the centroid name isn't
    # already in the dictionary, create the key and add the label to a list.
    # If the centroid name is already in the dictionary, append the new label
    # to the existing list.
    new_cent_dict = {}
    count = 0
    for element in list_of_points:
        cent_of_point = get_closest_centroid(element, centroids_dict)
        if cent_of_point not in new_cent_dict:
            new_cent_dict[cent_of_point] = [labels[count]]
        else:
            new_cent_dict[cent_of_point].append(labels[count])
        count += 1
    return new_cent_dict


def majority_count(labels):
    """Return the count of the majority labels in the label list

    Arguments:
        labels: a list of labels

    Returns: the count of the majority labels in the list

    Example:
        Code:
            labels = [0, 3, 3, 2, 2, 3, 4, 5, 5, 5, 4, 3, 2, 2, 2, 2]
            print(majority_count(labels))
        Output:
            6
    """

    labels_dict = {}
    high_count = 0

    # Create a dictionary where keys are integers denoting possible labels
    # and values are counts of that label.
    for element in labels:
        if element not in labels_dict:
            labels_dict[element] = 1
        else:
            labels_dict[element] += 1

    # Go through the values in this dictionary and find/return the highest
    # value
    for total in labels_dict.values():
        if total > high_count:
            high_count = total
    return high_count


def accuracy(list_of_points, labels, centroids_dict):
    """Calculate the accuracy of the algorithm. You should use
    update_assignment and majority_count (that you previously implemented)

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of ints representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a float representing the accuracy of the algorithm

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            labels = [2, 1, 3]
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                              "centroid2": [2, 2, 2, 2]}
            print(accuracy(list_of_points, labels, centroids_dict))
        Output:
            0.6666666666666666
    """

    # Create a new updated dictionary for all of the data points containing
    # labels as the values in the list
    new_label_dict = update_assignment(list_of_points, labels, centroids_dict)
    maj_label_count = 0
    total_label_count = 0

    # For each centroid in the new updated dictionary, find the number of
    # majority labels and the number of labels in the centroid and add them
    # to a accumulative count.
    for key, value in new_label_dict.items():
        maj_label_count += majority_count(value)
        total_label_count += len(value)
    return maj_label_count / total_label_count


# ----------------------------------------------------------
# HELPER FUNCTIONS
def setup_for_tests():
    """Creates are returns data for testing analysis methods.

    Returns: data, a list of data points
             labels, numeric labels for each data point
             centroids_dict1, three 4D centroids
             centroids_dict2, three non-random 4D centroids
                with poor starting values
    """

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    list_of_points = [
            [-1.01714716,  0.95954521,  1.20493919,  0.34804443],
            [-1.36639346, -0.38664658, -1.02232584, -1.05902604],
            [1.13659605, -2.47109085, -0.83996912, -0.24579457],
            [-1.48090019, -1.47491857, -0.6221167,  1.79055006],
            [-0.31237952,  0.73762417,  0.39042814, -1.1308523],
            [-0.83095884, -1.73002213, -0.01361636, -0.32652741],
            [-0.78645408,  1.98342914,  0.31944446, -0.41656898],
            [-1.06190687,  0.34481172, -0.70359847, -0.27828666],
            [-2.01157677,  2.93965872,  0.32334723, -0.1659333],
            [-0.56669023, -0.06943413,  1.46053764,  0.01723844]
        ]
    labels = [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]
    centroids_dict1 = {
            "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
            "centroid2": [-0.71767545, 1.2309971, -1.00348728, -0.38204247],
            "centroid3": [-1.71767545, 0.29971, 0.00328728, -0.38204247],
        }
    centroids_dict2 = {
            "centroid1": [0.1839742, -0.45809263, -1.91311585, -1.48341843],
            "centroid2": [10, 10, 10, 10],
            "centroid3": [-10, 1, -10, 10],
        }
    return list_of_points, labels, centroids_dict1, centroids_dict2


# ----------------------------------------------------------
# TESTS
def test_update_assignment():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # set up
    (list_of_points, labels,
     centroids_dict1, centroids_dict2) = setup_for_tests()

    # test with centroids_dict1
    answer = {'centroid3': [0, 1, 2, 1, 2, 2, 0], 'centroid1': [0],
              'centroid2': [1, 0]}

    assert_equals(answer,
                  update_assignment(list_of_points, labels, centroids_dict1))

    # test with centroids_dict2
    answer = {'centroid1': [0, 1, 0, 2, 1, 2, 1, 2, 0, 0]}
    assert_equals(answer,
                  update_assignment(list_of_points, labels, centroids_dict2))

    # test to make sure parameters remains unchanged
    # If you're failing this test,
    # make sure your code doesn't modify the parameters passed in
    (list_of_points_copy, labels_copy,
     centroids_dict1_copy, centroids_dict2_copy) = setup_for_tests()
    assert_equals(list_of_points, list_of_points_copy)
    assert_equals(labels, labels_copy)
    assert_equals(centroids_dict1, centroids_dict1_copy)
    assert_equals(centroids_dict2, centroids_dict2_copy)

    print("test_update_assignment passed")


def test_majority_count():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # single
    assert_equals(6, majority_count([0, 0, 0, 0, 0, 0]))
    assert_equals(5, majority_count([1, 0, 0, 0, 0, 0]))
    assert_equals(5, majority_count([0, 1, 1, 1, 1, 1]))

    # mixed
    assert_equals(4, majority_count([0, 0, 1, 1, 0, 0]))
    assert_equals(4, majority_count([0, 2, 2, 2, 3, 3, 0, 1, 1, 0, 0]))

    # tied max count
    assert_equals(4, majority_count([0, 2, 2, 2, 0, 2, 0, 0]))

    # test with labels outside of 1-10
    assert_equals(6,
                  majority_count(["cat", "cat", "cat", "cat", "cat", "cat"]))

    print("test_majority_count passed")


def test_accuracy():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    # set up
    (list_of_points, labels,
     centroids_dict1, centroids_dict2) = setup_for_tests()

    # test with centroids_dict1
    expected = 0.5
    received = accuracy(list_of_points, labels, centroids_dict1)
    assert_equals(expected, received)

    # test with centroids_dict2
    expected = 0.4
    received = accuracy(list_of_points, labels, centroids_dict2)
    assert_equals(expected, received)

    # test to make sure parameters remains unchanged
    # If you're failing this test,
    # make sure your code doesn't modify the parameters passed in
    (list_of_points_copy, labels_copy,
     centroids_dict1_copy, centroids_dict2_copy) = setup_for_tests()
    assert_equals(list_of_points_copy, list_of_points)
    assert_equals(labels_copy, labels)
    assert_equals(centroids_dict1_copy, centroids_dict1)
    assert_equals(centroids_dict2_copy, centroids_dict2)

    print("test_accuracy passed")


def main_test():

    #######################################################
    # You do not need to change anything in this function #
    #######################################################

    test_update_assignment()
    test_majority_count()
    test_accuracy()
    print("all tests passed.")


if __name__ == "__main__":
    centroids = load_centroids("mnist_final_centroids.csv")
    # Consider exploring the centroids data here

    # Uncomment the line below for Part 2 Step 2, 3, and 4:
    # main_test()

    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))

# 1. What happened to the centroids? Why are there fewer than 10?

# Answer:
# After running kmeans.py on the MNIST data, the 10 original centroids,
# after convergence, turned into only 9 centroids. After analyzing the
# final images I noticed that there were two centroids that appeared to be of
# the number 9 and 6, while the numbers 4,5,8 didn't appear to be there. This
# seemed to be caused by clustering of the images 3,4,5,6,8, as similarity in
# these numbers caused more errors to occur when updating assignment. As after
# one cycle centroid4 had already been removed from the dictionary, as it had
# no data points that were closest to it.

# 2. What's the accuracy of the algorithm on MNIST? By looking at the
# centroids, which digits are easier to be distinguished by the algorithm,
# and which are harder?

# Answer:
# The accuracy of the algorithm on MNIST is 0.582. By looking at the centroids
# it appears that 0, 1, 2, 6, 7 and 9 are the digits that the algorithm was
# able to distinguish the best. While 3, 4, 5, 8 were all harder to
# distinguish from each other, as faint outlines of each digit can be seen in
# centroid6 and especially centroid1.
