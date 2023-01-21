def twoSum(nums, target):
    hash_map={}
    # we will use hash_map to store the values as keys and indices as values.
    for i, j in enumerate(nums):
        remaining = target - j
        # Here remaining in hash_map.keys() would also work
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[j] = i
