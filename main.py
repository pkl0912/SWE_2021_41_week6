from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    num_indices = {}
    
    for i, num in enumerate(nums):
 
        complement = target - num

        if complement in num_indices:
  
            return [num_indices[complement], i]

        num_indices[num] = i

    return []


nums = input("Enter a list of numbers with spaces: ").split()
nums = [int(num) for num in nums]
target = int(input("Enter the target number: "))


output = twoSum(nums, target)

print(output)