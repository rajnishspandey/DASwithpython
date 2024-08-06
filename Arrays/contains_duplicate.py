#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false
array = [1,2,3,1]
def check_duplicates(array): #[1,2,3,1]
    array.sort() #O(nlogn)
    # [1,1,2,3]
    for i in range(len(array)-1): #0,1,2,3
        if array[i] == array[i+1]:
            return True
        else:
            return False
        
# print(check_duplicates(array))

# solution 2 
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
def smart_duplicate_search(array):
    dictionary = {}
    for item in array:
        if item in dictionary:
            return True
        dictionary[item] = True
    return False

print(smart_duplicate_search(array))  # Output: True
