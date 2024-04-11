
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Save the numbers with their indices
    num_dict = {}

    # Loop through the list of numbers
    for i, num in enumerate(nums):

        # Calculate the complement
        complement = target - num

        # If the complement in the dict, return the index of that complement and the current number's index
        
        if complement in num_dict:
            return [num_dict[complement], i]

        # Add the current number to the dictionary
        num_dict[num] = i

    return