# python 3

# Binary search pseudo code template

# define function boolean IsInArray(startElement: number, endElement: number, elementToFind: number,
# elements: array of number)
# {
#     boolean found = false
# integer index = (endElement + startElement) / 2
#
# # Look in the middle
# if (elements[index] = elementToFind)
# {
# return true
# }
#
# # Go to the right
# if (elementToFind > elements[index])
# {
# return IsInArray(index + 1, endElement, elementToFind, elements)
# }
#
# # Go to the left
# if (elementToFind < elements[index])
# {
# return IsInArray(startElement, index - 1, elementToFind, elements)
# }
#
# return false;
# }
#
# define numbers = [2, 8, 22, 44, 56, 65, 72, 101, 208, 452, 801]
#
# Print IsInArray(0, numbers.Count - 1, 22, numbers)


# ----------------------------  HOMEWORK #4  ----------------------------
# binary search requirement; array must be sorted


def is_in_array(start, end, find, elements):
    """
    binary search by function defines if a given element can be found in the array and ultimately
    if the element was found

    :param start: index of array where search starts
    :type start: integer
    :param end: index of array where search ends
    :type end: integer
    :param find: the element to find
    :type find: integer
    :param elements: sorted list/array of elements where function searches for param find
    :type elements: list of integers
    :return: True or False
    :rtype: Boolean
    """

    index_ = (end + start) // 2

    if start <= end:

        # Look in the middle
        if elements[index_] == find:
            print("{} is found at index {}".format(find, index_))
            return True

        # Go to the right
        if find > elements[index_]:
            return is_in_array(index_ + 1, end, find, elements)

        # Go to the left
        if find < elements[index_]:
            return is_in_array(start, index_ - 1, find, elements)

    return False


numbers = [2, 8, 22, 44, 56, 65, 72, 101, 208, 452, 801]
find_number = 22
initial_start = 0
initial_end = len(numbers) - 1
print(is_in_array(initial_start, initial_end, find_number, numbers))
