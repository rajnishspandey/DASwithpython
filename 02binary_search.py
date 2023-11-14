def binary_search(list, target):
    first = 0
    last = len(list)-1 #to find the last value index

    while first <= last:
        midpoint = (first + last)//2

        if list(midpoint) == target:
            return midpoint
        elif list(midpoint) < target:
            first = midpoint + 1
        else:
            last = midpoint - 1


