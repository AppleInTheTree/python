# 5. Longest Palindropm Substring

# two pointer
def longestPaildrome(s : str) ->str:
    def expend(left: int, right: int) ->str:
        #two pointer
        while left >= 0 and right <=len(s) and s[left] == s[right -1]:
            left -= 1
            right +=1
        return s[left + 1 : right + 1]

    res =''
    for i in range(0, len(s)-1):
        res = max(res, expend(s, i, i+1), expend(s, i, i+2, key = len))
    if len(s) < 2 or s ==s[::-1]:
        return s

    return res


    # class Solution:
	# def longestPalindrome(self, s: str) -> str:
	# 	res = ""
	# 	length = len(s)
	# 	def helper(left: int, right: int):
	# 		while left >= 0 and right < length and s[left] == s[right]:
	# 			left -= 1
	# 			right += 1
				
	# 		return s[left + 1 : right]
		
		
	# 	for index in range(len(s)):
	# 		res = max(helper(index, index), helper(index, index + 1), res, key = len) res와 홀수 짝수 탐색한것을 반환해서 max로 변환 
			
	# 	return res