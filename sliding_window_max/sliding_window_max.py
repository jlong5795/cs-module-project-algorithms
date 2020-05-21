'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # inputs: array of ints and an int that is the "window size"
    # make a pointer to start at the beginning of the array
    # evaluate the starting pointer and additional values to equal number given
    # add the greatest of those values to a solution array
    # increment the pointer

    max = 0
    solution = []

    for i in range(len(nums) - k + 1):# resolves to 6
        max = nums[i]
        for j in range(1,k):
            if nums[i + j] > max:
                max = nums[i + j]
        solution.append(max)

    return solution


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
