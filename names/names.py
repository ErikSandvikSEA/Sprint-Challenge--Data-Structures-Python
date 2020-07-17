import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# |||||||||||||||| YUCK O(n^2) BECAUSE NESTED FOR LOOP ||||||||||||||||||||||

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# +++++++++++++++++++++++++ BST ++++++++++++++++++++++
# Looks like between 0.06sec and 0.10 sec

# from binary_search_tree import BSTNode

# establish the root node w/first name in the list
# root_node = BSTNode(names_1[0])

# add all the names from names_1 to the tree
# for name1 in names_1:
#     root_node.insert(name1)

# check the BST for any duplicates when passing through names_2
# for name2 in names_2:
# if the name is already in the BST, append it to our duplicates list
#     if root_node.contains(name2):
#         duplicates.append(name2)
# +++++++++++++++++++++++++ END BST +++++++++++++++++++

# ************************* FREQUENCY COUNTER *********************
# Looks like between 0.004 and 0.010 seconds

# # establish a counter dict
# name_counter = {}

# # add all names from names_1 to name_counter
# for name1 in names_1:
#     name_counter[name1] = True

# # check names_2, if the name is already in the counter, append it to duplicates
# for name2 in names_2:
#     if name2 in name_counter:
#         duplicates.append(name2)

# *********************** END FREQUENCY COUNTER *******************

# ()()()()()()()()()()()()()()()()() ARRAY/LIST CHECK ()()()()()()()()()()()()()()()()()
# Looks like between 1.3 and 1.6 seconds

# for name1 in names_1:
#     if name1 in names_2:
#         duplicates.append(name1)

# ()()()()()()()()()()()()()()()()END ARRAY/LIST CHECK ()()()()()()()()()()()()()()()()

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
