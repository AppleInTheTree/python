# 1. two sum
# def twoSum(nums : list[int], target : int) ->list[int]:
#     for i in len(nums):
#         for a in (i+1, len(nums)):
#             if nums[i] + nums[a] == target:
#                 return [i,a]


#해쉬 테이블을 이용한 구현 
def twoSum(nums : list[int], target : int) ->list[int]:
    nums_map ={}

    for i, n in enumerate(nums):
        nums_map[n] = i

    for i, n in enumerate(nums):
        if target - n in nums_map and i !=nums_map[target -n]:
            return nums.index(n), nums_map[target -n]

#투포인터를 이요안 구현(할수가 없다.)N  num.sort()를 쓰면 index가 엉망이된다

def twoSumm(nums : list[int], target : int) ->list[int]:
    left , right = 0 , len(nums) - 1

    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] +nums[right] > target:
            right -=1
        else:
            return [left, right]
    


