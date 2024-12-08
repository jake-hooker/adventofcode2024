from time import perf_counter

"""
Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

What is the total of all of these distances?

"""

def process_input(input_file):
    """Read the input file and split it into two lists
    args: input_file (str): path to the input file

    returns: two sorted lists (left, right) of integers
    """

    left = list()
    right = list()

    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            new = line.split()
            left.append(int(new[0]))
            right.append(int(new[1]))
    file.close()

    return sort_list(left), sort_list(right)

def sort_list(list):
    """Sort a list in ascending order

    args: list (list): list of integers

    returns: sorted list
    """
    list.sort()

    return list

def calculate_distances(left, right):
    """Calculate the total distance between two equal length sorted lists
    
    args: left (list): a list of integers of len(n)
          right (list): a list of integers of len(n)
        
    returns: total_distance (int): total distance between the two lists
    """
    total_distance = 0
    for i, j in zip(left, right):
        total_distance += abs(i - j)

    return total_distance

def calculate_similarity(left, right):
    """Calculate the similarity score between two sorted lists
    
    args: left (list): a list of integers
          right (list): a list of integers
        
    returns: similarity_score (int): similarity score between the two lists
    """
    total_similarity_score = 0

    for element in left:
        total_similarity_score += (element * right.count(element))

    return total_similarity_score

if __name__ == "__main__":
    t1_start = perf_counter() 
    left, right = process_input('../inputs/day1.txt')
    print("Total distance:", calculate_distances(left, right))
    print("Similarity score:", calculate_similarity(left, right))
    t1_stop = perf_counter()
    print("Elapsed time:", t1_stop-t1_start)