'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # iterate through the array looking at each value
    for each in arr:
        # evaluate if the value is a non-zero value
        if each == 0:
            # pop it out of the array
            arr.remove(each)
            # insert it at the beginning
            arr.append(0)
    print(arr)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    moving_zeroes(arr)
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")