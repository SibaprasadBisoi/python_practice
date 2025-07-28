def find_two_nums(sum):
    seen = {}
    for num in numbers:
        diff = target - num
        if diff in seen:
            return diff, num
        seen[num] = True
    return None
nums = [5, 6, 6, 3, 5]
target = 9
result = find_two_nums(nums, target)
if result:
    print(f'Found numbers: {result[0]} + {result[1]} = {target}')
else:
    print(f"No numbers found whose sum is {target}")