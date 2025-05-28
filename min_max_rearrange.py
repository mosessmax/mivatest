def alternate_min_max_rearrangement(arr):
    if not arr:
        return []
    
    sorted_arr = sorted(arr)
    result = []
    left = 0
    right = len(sorted_arr) - 1
    
    # alternate between picking smallest and largest
    pick_smallest = True
    
    while left <= right:
        if pick_smallest:
            result.append(sorted_arr[left])
            left += 1
        else:
            result.append(sorted_arr[right])
            right -= 1
        
        pick_smallest = not pick_smallest
    
    return result


def main():
    # test cases from the problem
    test_cases = [
        [13, 7, 8, 3, 2, 10, 15, -1],
        [-5, -12, -1, 7, 14, -7, 3, 6],
        [3, 6, 9, -10, -5, -2, 0, 8]
    ]
    
    expected_outputs = [
        [-1, 15, 2, 13, 3, 10, 7, 8],
        [-12, 14, -7, 7, -5, 6, -1, 3],
        [-10, 9, -5, 8, -2, 6, 0, 3]
    ]
    
    for i, arr in enumerate(test_cases):
        result = alternate_min_max_rearrangement(arr)
        print(f"Input: {arr}")
        print(f"Output: {result}")
        print(f"Expected: {expected_outputs[i]}")
        print(f"Match: {result == expected_outputs[i]}")
        print()


if __name__ == "__main__":
    main()