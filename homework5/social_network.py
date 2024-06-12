# Name: Jaiden Atterbury
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()

    practice_graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'),
                                   ('B', 'D'), ('C', 'D'), ('C', 'F'),
                                   ('D', 'E'), ('D', 'F')])

    return practice_graph


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()
    rj.add_edges_from([("Juliet", "Nurse"), ("Juliet", "Tybalt"),
                       ("Juliet", "Capulet"), ("Juliet", "Friar Laurence"),
                       ("Juliet", "Romeo"), ("Tybalt", "Capulet"),
                       ("Capulet", "Escalus"), ("Capulet", "Paris"),
                       ("Friar Laurence", "Romeo"), ("Romeo", "Benvolio"),
                       ("Romeo", "Montague"), ("Romeo", "Mercutio"),
                       ("Benvolio", "Montague"), ("Montague", "Escalus"),
                       ("Escalus", "Paris"), ("Escalus", "Mercutio"),
                       ("Paris", "Mercutio")])

    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    # For each friend of the user, find their immediate friends. Through each
    # iteration, take the union of the two sets. In order to remove the user
    # and any of the users's friends, take the set difference of the final set
    # and a set including the user and any of the users's friends.
    return_set = set()
    for useri in friends(graph, user):
        return_set = return_set | friends(graph, useri)
    return return_set - ({user} | friends(graph, user))


def common_friends(graph, user1, user2):
    """
    Finds and returns the set of friends that user1
    and user2 have in common.`

    Arguments:
        graph:  the graph object that contains the users
        user1: a unique identifier representing one user
        user2: a unique identifier representing another user
`
    Returns: a set containing the friends user1 and user2 have in common
    """
    # To find the set of friends that user1 and user2 have in common, simply
    # take the intersection of their individual friend sets.
    return friends(graph, user1) & friends(graph, user2)


def num_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      num_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    # For each friend of friend of the user, add them (key) and the number of
    # mutual friends (value) into the dictionary.
    num_com_dict = {}
    for useri in friends_of_friends(graph, user):
        num_com_dict[useri] = len(common_friends(graph, user, useri))
    return num_com_dict


def num_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    # Start by default sorting through the items of the dictionary, then
    # sort by the value. Once this is done iterate through this list and
    # append the first element of each tuple (the key) to the return list.
    # This could also be done through the use of a list comprehension:
    # return [tup[0] for tup in sort_nums].
    sort_natural = sorted(map_with_number_vals.items())
    sort_num = sorted(sort_natural, key=itemgetter(1),
                      reverse=True)
    key_list = []
    for tup in sort_num:
        key_list.append(tup[0])
    return key_list


def recs_by_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a unique identifier

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    # Create a dictionary with the number of common friends the user has with
    # each friend of friend. Then find a list of friend recommendations for the
    # user.
    rec_dict = num_common_friends_map(graph, user)
    return num_map_to_sorted_list(rec_dict)

###
#  Problem 3
###


def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    # For each friend of friend the user has, find the influence score. Add
    # this friend of friend (key) and their influence score (value) to the
    # influence dictionary.
    influence_dict = {}
    for useri in friends_of_friends(graph, user):
        influence_score = 0
        for userj in common_friends(graph, user, useri):
            influence_score += 1 / len(friends(graph, userj))
        influence_dict[useri] = influence_score
    return influence_dict


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    # Create a dictionary with the influence score user has with each
    # friend of friend. Then find a list of friend recommendations for the
    # user.
    rec_dict = influence_map(graph, user)
    return num_map_to_sorted_list(rec_dict)


###
#  Problem 5
###

def get_facebook_graph(filename):
    """Builds and returns the facebook graph
    Arguments:
        filename: the name of the datafile
    """
    # Open the file at filename and create a blank graph. For each line in
    # the given file, split the string into a list of two ints. For each of
    # these two ints, add an edge in fb_graph. Close the file and return the
    # graph.
    my_file = open(filename)
    fb_graph = nx.Graph()
    for line in my_file:
        values = line.split()
        fb_graph.add_edge(int(values[0]), int(values[1]))
    my_file.close()
    return fb_graph


def test_get_facebook_graph(facebook, filename):
    if (filename == "facebook-links-small.txt"):
        pass
    else:
        assert len(facebook.nodes()) == 63731
        assert len(facebook.edges()) == 817090


def main():
    # practice_graph = get_practice_graph()
    # Comment out this line after you have visually verified your practice
    # graph.
    # Otherwise, the picture will pop up every time that you run your program.
    # draw_practice_graph(practice_graph)

    rj = get_romeo_and_juliet_graph()
    # Comment out `this line after you have visually verified your rj graph and
    # created your PDF file.
    # Otherwise, the picture will pop up every time that you run your program.
    # draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()

    # Create two empty lists, for each person in the rj graph, if both
    # recommendations yield the same list, add the person to the not changed
    # list. If they yield different lists, add the person to the changed list.
    not_changed_list = []
    changed_list = []
    for user in rj.nodes():
        if recommend_by_influence(rj, user) == recs_by_common_friends(rj,
                                                                      user):
            not_changed_list.append(user)
        else:
            changed_list.append(user)
    print("Unchanged Recommendations:", sorted(not_changed_list))
    print("Changed Recommendations:", sorted(changed_list))

    ###
    #  Problem 5
    ###

    # (replace this filename with "facebook-links-small.txt" for testing)
    fb_filename = "facebook-links-small.txt"
    fb_graph = get_facebook_graph(fb_filename)

    # test_get_facebook_graph(fb_graph, fb_filename)

    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()

    # For each node in the fb_graph, if the id is divisible by 1000, add it to
    # the a list that will be used to recommend certain friends.
    node_list = []
    for id in sorted(list(fb_graph.nodes())):
        if id % 1000 == 0:
            node_list.append(id)

    # For each id in the list that contains id's divisble by 1000, find and
    # print the top 10 recommendations by number of common friends.
    for id in node_list:
        num_recs = recs_by_common_friends(fb_graph, id)
        print(id, "(by num_common_friends):", num_recs[:10])

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()

    # For each id in the list that contains id's divisible by 1000, find and
    # print the top 10 recommendations by influence score.
    for id in node_list:
        infl_recs = recommend_by_influence(fb_graph, id)
        print(id, "(by influence):", infl_recs[:10])

    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()

    # Create two counts, for each person in the fb graph, if both
    # recommendations yield the same list, increment the same count.
    # If the recommendations yield different lists, increment the different
    # count.
    same_count = 0
    different_count = 0
    for id in node_list:
        if recommend_by_influence(fb_graph, id) == recs_by_common_friends(
                                                              fb_graph, id):
            same_count += 1
        else:
            different_count += 1
    print("Same:", same_count)
    print("Different:", different_count)


if __name__ == "__main__":
    main()


###
#  Collaboration
###

# On Homework 5 Check-in, Part 1, and Part 2, I collaborated with no one when
# writing the code. However, Tanner Huck and I briefly looked at each others
# code to make sure we weren't missing anything/got the same output.
