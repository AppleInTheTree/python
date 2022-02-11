def array_front9(nums):
  for i in range(len(nums)):
    if i < 4:
      if nums[i] == 9:
        return True
      else:
        return False
    else:
      return False
a = [1,2,9,3,4]


b = array_front9(a)
print(b)