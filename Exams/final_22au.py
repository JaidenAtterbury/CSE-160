# Name: Jaiden Atterbury
# CSE 160
# Autumn 2022
# Final Exam

from math import isclose
from operator import itemgetter


# Problem 1
def create_match(my_team, score_sheet):
    """
    Arguments:
        my_team (string): the team you are making a match for
        score_sheet (dict): a dictionary where the keys are the team names
                        and values are a tuple of lists of the form:
                        ([teams won against], [teams lost against])
    Returns:
        a tuple of (chosen opponent team, winning average)
        where chosen opponent team is the team with the lowest winning average
        and winning average is the winning average of that team.
    """
    # For each team in score_sheet, if the team is not my_team, find their
    # winning percentage. If this winning percentage is the current smallest
    # set win_avg to temp_avg and opponent to the team with the current lowest
    # winning percentage. After looping through all of the teams, return the
    # tuple containing the opponent and their winning percentage.
    win_avg = None
    opponent = ""
    for team, scores in score_sheet.items():
        num_won = 0
        num_lost = 0
        temp_avg = 0
        if team != my_team:
            num_won = len(scores[0])
            num_lost = len(scores[1])
            temp_avg = num_won / (num_lost + num_won)
            if win_avg is None or temp_avg < win_avg:
                win_avg = temp_avg
                opponent = team
    return (opponent, win_avg)


def test_match(actual, expected):
    assert actual[0] == expected[0]
    assert isclose(actual[1], expected[1])


def test_create_match():
    scores1 = {"USA": (["France", "Brazil"], ["Korea"]),
               "France": (["Brazil"], ["USA"]),
               "Brazil": (["Korea"], ["France", "USA"]),
               "Korea": (["USA"], ["Brazil"])}
    test_match(create_match("USA", scores1), ("Brazil", 0.3333333333333333))

    scores2 = {"USA": (["France"], []),
               "France": ([], ["USA"])}
    test_match(create_match("USA", scores2), ("France", 0))

    scores3 = {"USA": (["France"], ["Brazil"], []),
               "France": ([], ["USA"]),
               "Brazil": ([], ["USA"])}
    test_match(create_match("USA", scores3), ("France", 0))
    test_match(create_match("Brazil", scores3), ("France", 0))

    print("test_create_match passed!")


# Problem 2
def search_item(inventory, search_terms, num_match):
    """
    Arguments:
        inventory (dict): a dictionary where each key is an item (string)
        and each value is a list of (string) descriptive terms that apply to
        the item.
        search_terms (list): a list of strings representing the descriptive
        terms being searched for
        num_match (integer): the number of descriptive terms from search_terms
        that need to be in an item's list of descriptive terms before that item
        would be returned.

    Returns:
        an alphabetically sorted list of items who have at least num_match
        terms from search_terms in their list of descriptive terms.
    """
    # For each of the items in the inventory, loop through the search terms
    # and count the number of matching words. If the number of similar words
    # is less than or equal to the number of required matches, add this item
    # to the list of matches. At the end return this list of matches.
    match_list = []
    for item, description in inventory.items():
        num_same = 0
        for search in search_terms:
            if search in description:
                num_same += 1
        if num_same >= num_match:
            match_list.append(item)
    return match_list


def test_search_item():
    inventory1 = {"banana": ["yellow", "long", "Fruit"],
                  "pole": ["long", "plastic"],
                  "yellow wig": ["wavy", "hair", "long", "yellow"],
                  "chair": ["furniture", "brown"]}
    search_terms1 = ["long", "yellow", "Fruit", "tangy"]
    search_terms2 = ["yellow", "long", "brown", "Fruit", "wavy"]
    assert search_item(inventory1,
                       search_terms1, 2) == ["banana", "yellow wig"]
    assert search_item(inventory1, search_terms1, 4) == []
    assert search_item(inventory1, search_terms2, 1) == ["banana",
                                                         "pole",
                                                         "yellow wig",
                                                         "chair"]
    assert search_item(inventory1, search_terms2, 3) == ["banana",
                                                         "yellow wig"]

    print("test_search_item passed!")


# Problem 3
def todo_list(tasks):
    """
    Arguments:
        tasks (list): a list of dictionaries where each dictionary
            represents a task with the keys "name",
            "priority", "time req", and "completed"

    Returns: a list of task names that are not completed, sorted by priority
             and time required.
    """
    # For each dictionary in the task list, if the task isn't already done,
    # create a tuple of the name, priority, and time required for the task.
    # Then add this tuple to the task list. Once this task list is found,
    # since priority is the main sorting feature, sort the list by time
    # required, then by priotiy. Once this list is sorted, loop through the
    # list to obtain all of the names of the tasks left to do, then return
    # this list of sorted taks.
    task_list = []
    sorted_list = []
    for dict in tasks:
        todo_tup = tuple()
        if dict["completed"] is False:
            todo_tup = (dict["name"], dict["priority"], dict["time req"])
            task_list.append(todo_tup)
    sort_by_time = sorted(task_list, key=itemgetter(2))
    sort_by_priority = sorted(sort_by_time, key=itemgetter(1))
    for index in range(len(sort_by_priority)):
        sorted_list.append(sort_by_priority[index][0])
    return sorted_list


def test_todo_list():
    tasks_lst1 = [{"name": "CSE160 HW6", "priority": 1,
                   "time req": 90, "completed": True},
                  {"name": "Grocery shopping", "priority": 2,
                   "time req": 20, "completed": False},
                  {"name": "Doing the Laundry", "priority": 1,
                   "time req": 60, "completed": False},
                  {"name": "Water plants", "priority": 2,
                   "time req": 10, "completed": False}]

    assert todo_list(tasks_lst1) == ["Doing the Laundry", "Water plants",
                                     "Grocery shopping"]

    tasks_lst2 = [{"name": "Eating Lunch", "priority": 1,
                   "time req": 30, "completed": True},
                  {"name": "Doing the dishes", "priority": 2,
                   "time req": 10, "completed": False},
                  {"name": "Making Lunch", "priority": 1,
                   "time req": 30, "completed": True}]
    assert todo_list(tasks_lst2) == ["Doing the dishes"]

    tasks_lst3 = [{"name": "CSE160 HW6", "priority": 1,
                   "time req": 90, "completed": True},
                  {"name": "Grocery shopping", "priority": 1,
                  "time req": 20, "completed": False},
                  {"name": "Doing the Laundry", "priority": 1,
                   "time req": 60, "completed": False},
                  {"name": "Water plants", "priority": 1,
                   "time req": 10, "completed": False}]
    assert todo_list(tasks_lst3) == ["Water plants", "Grocery shopping",
                                     "Doing the Laundry"]

    tasks_lst4 = [{"name": "CSE160 HW6", "priority": 1,
                   "time req": 90, "completed": True},
                  {"name": "Grocery shopping", "priority": 2,
                   "time req": 20, "completed": True},
                  {"name": "Doing the Laundry", "priority": 1,
                   "time req": 60, "completed": True},
                  {"name": "Water plants", "priority": 2,
                   "time req": 10, "completed": True}]
    assert todo_list(tasks_lst4) == []

    print("test_todo_list passed!")


def main():
    test_create_match()
    test_search_item()
    test_todo_list()


if __name__ == "__main__":
    main()


# You will answer a question about collaboration in part 2.
