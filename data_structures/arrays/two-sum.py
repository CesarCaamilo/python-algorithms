def two_sum(nums, target):
    # Create a dictionary to store the numbers and their indices
    num_indices = {}
    
    for index, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # If the complement is already in the dictionary, we found a solution
        if complement in num_indices:
            return [num_indices[complement], index]
        
        # Otherwise, store the current number's index in the dictionary
        num_indices[num] = index
    
    # No solution found
    return None

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1] (since nums[0] + nums[1] = 2 + 7 = 9)




