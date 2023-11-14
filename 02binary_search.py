def binary_search(list, target):
    first = 0
    last = len(list)-1 #to find the last value index

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def validate(index):
    if index is not None:
        print(f"Target found at the index : {index}")
    else:
        print("target not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers,12)
validate(result)

result = binary_search(numbers,8)
validate(result)