from typing import List


def maxSubarraySumCircular(nums:List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    s = sum(nums)
    curr_max = max_so_far = curr_min = min_so_far = nums[0]
    for i in range(1, len(nums)):
        # Kadane's algorithm to find maximum subarray sum.
        curr_max = max(curr_max + nums[i], nums[i])
        max_so_far = max(max_so_far, curr_max)
        # Kadane's algorithm to find minimum subarray sum.
        curr_min = min(curr_min + nums[i], nums[i])
        min_so_far = min(curr_min, min_so_far)

    if min_so_far == s:
        return max_so_far

    return max(max_so_far, s - min_so_far)