from random import shuffle
from math import sqrt


def list_2d_to_1d(lst_2d):
    return [element for row in lst_2d for element in row]
    # (for sublist in list_2d) gets the every row in this list
    # (for it in row) gets every element in this row


def list_1d_to_2d(lst_1d, size):
    return [lst_1d[i: i + size] for i in range(0, len(lst_1d), size)]
    # (for i in range(0, len(lst_1d), size)) iterate from 0 to len(lst_1d)
    # but every iteration it increases by size
    # (lst_1d[i: i + size]) gets the elements from i to i + size


def public_shuffle_2d_list(lst):
    flatten_list = list_2d_to_1d(lst)
    shuffle(flatten_list)
    return list_1d_to_2d(flatten_list, len(lst[0]))
    # Convert the 2d list to 1d
    # Shuffle the 1d list
    # Convert the 1d list to 2d


def distance_between_2_points(x, y, x1, y1):
    return sqrt((x - x1)**2 + (y - y1)**2)


def coordinates_1d_to_2d(index, n):
    x = int((index - 1) / n)
    y = int((index - 1) % n)
    return x, y


def coordinates_2d_to_1d(x, y):
    return ((x + 1) * y) + x + 1
