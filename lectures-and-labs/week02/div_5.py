#Completion
def findMiddleElement(arr):
    """
    This function finds the middle element of an array.
    If the array has an odd length, it returns the middle element.
    If the array has an even length, it returns the average of the two middle elements.
    
    :param arr: List of numbers
    :return: Middle element or average of two middle elements
    """
    n = len(arr)
    if n == 0:
        return None
    elif n % 2 == 1:
        return arr[n // 2]
    else:
        mid1 = arr[n // 2 - 1]
        mid2 = arr[n // 2]
        return (mid1 + mid2) / 2


def findStartElement(arr):
    """Return the first element of an array, or None if it is empty."""
    if len(arr) == 0:
        return None
    return arr[0]


def findEndElement(arr):
    """Return the last element of an array, or None if it is empty."""
    if len(arr) == 0:
        return None
    return arr[-1]