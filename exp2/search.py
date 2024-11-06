def linear_search(arr, x):
    """
    Perform a linear search for x in arr.
    Returns the index of x if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binary_search(arr, x):
    """
    Perform a binary search for x in sorted arr.
    Returns the index of x if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# Test cases
def test_search_algorithms():
    test_cases_linear = [
        ([1, 2, 3, 4, 5], 3, 2),  # Found, positive
        ([10, 20, 30, 40, 50], 20, 1),  # Found, positive
        ([7, 8, 9, 10], 11, -1),  # Not found, negative
        ([1, 2, 3, 4, 5], 6, -1),  # Not found, negative
        ([5, 5, 5, 5, 5], 5, 0),  # Found (multiple occurrences), positive
    ]

    test_cases_binary = [
        ([1, 2, 3, 4, 5], 3, 2),  # Found, positive
        ([10, 20, 30, 40, 50], 30, 2),  # Found, positive
        ([1, 3, 5, 7, 9], 8, -1),  # Not found, negative
        ([2, 4, 6, 8, 10], 5, -1),  # Not found, negative
        ([10, 20, 30, 40, 50], 50, 4),  # Found, positive
    ]

    print("Linear Search Test Cases:")
    for arr, x, expected in test_cases_linear:
        result = linear_search(arr, x)
        print(f"Array: {arr}, Target: {x}, Expected: {expected}, Got: {result}")

    print("\nBinary Search Test Cases:")
    for arr, x, expected in test_cases_binary:
        result = binary_search(arr, x)
        print(f"Array: {arr}, Target: {x}, Expected: {expected}, Got: {result}")


# Run the tests
test_search_algorithms()
