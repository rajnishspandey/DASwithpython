def linear_search(list,target):
    """
    retuns the index position of the target if found, eles return None
    """

    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None


def validate(index):
    if index is not None:
        print(f"Target found at the index : {index}")
    else:
        print("Target not found")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers,12)
validate(result)

result = linear_search(numbers,10)
validate(result)