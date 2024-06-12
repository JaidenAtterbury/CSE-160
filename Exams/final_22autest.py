import networkx as nx
from operator import itemgetter
import matplotlib.pyplot as plt

# Problem 2

goals_dict = {}
goals_file = "goals.txt"
goals_open = open(goals_file)
for line in goals_open:
    values = line.split()
    country = values.pop(0)
    int_values = [int(i) for i in values]
    temp_min = min(int_values)
    if country in goals_dict:
        if temp_min < goals_dict[country]:
            goals_dict[country] = temp_min
    else:
        goals_dict[country] = temp_min
goals_open.close()
print(goals_dict)

# Problem 3


def clean_graph(input_graph):
    """
    Returns a graph corresponding to input_graph that contains
    the same edges and nodes, but where all nodes are integers
    and trailing characters "fb" have been removed.
    """
    cleaned_graph = nx.Graph()
    for edge in input_graph.edges():
        new_edge = []
        for item in edge:
            temp_node = int(item[:-2])
            new_edge.append(temp_node)
        cleaned_graph.add_edge(new_edge[0], new_edge[1])
    return cleaned_graph


g = nx.Graph()
g.add_edge("367fb", "368fb")
g.add_edge("369fb", "370fb")
print(g.edges())
print(g.nodes())

new_graph = clean_graph(g)
print(new_graph.edges())
print(new_graph.nodes())

# Problem 4
fall_enroll = [('CSE 160', 'Ruth Anderson', 180),
               ('CSE 446', 'Ruth Anderson', 180),
               ('CSE 446', 'Brett Wortzman', 200),
               ('CSE 446', 'Brett Wortzman', 180)]

expected = [('CSE 160', 'Ruth Anderson', 180),
            ('CSE 446', 'Brett Wortzman', 200),
            ('CSE 446', 'Brett Wortzman', 180),
            ('CSE 446', 'Ruth Anderson', 180)]

sorted_by_prof = sorted(fall_enroll, key=itemgetter(1))
sorted_by_size = sorted(sorted_by_prof, key=itemgetter(2), reverse=True)
output_list = sorted(sorted_by_size, key=itemgetter(0))

print(output_list)
print(expected)

# Problem 9

plt.plot([1, 2, 3, 4, 5, 6], [10, 2, 8, 1, 6, 5])
plt.xlabel("Day")
plt.ylabel("Visitor Count")
plt.title("Visitors per Day")
plt.savefig("visitors.png")
plt.show()
