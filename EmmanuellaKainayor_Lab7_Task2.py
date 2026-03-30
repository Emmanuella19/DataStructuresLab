# Task is to Write a recursive method named ‘print_subsets(arr)’ that takes a Python list as input and prints all possible subsets as a list.
def print_subsets(arr, index=0, current_subset=[]):
    # Base case: if the index is equal to the length of the array, print the current subset
    if index == len(arr):
        print(current_subset)
        return

    # Recursive case: include the current element in the subset and move to the next element
    print_subsets(arr, index + 1, current_subset + [arr[index]])

    # Recursive case: exclude the current element from the subset and move to the next element
    print_subsets(arr, index + 1, current_subset)

# driver code
if __name__ == "__main__":
    arr = [1, 2, 3]
    print_subsets(arr)