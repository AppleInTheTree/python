# 1689. Partitioning into Minumum Numbers Of Deci Binary Number
# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

# Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

 

# Example 1:

# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32
# Example 2:

# Input: n = "82734"
# Output: 8
# Example 3:

# Input: n = "27346209830709182346"
# Output: 9

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)

# 1과 0으로만 이루어진 십진수를 이용하여 해당 숫자를 만들어야 한다. 이때 더해야하는 mim 횟수를 리턴
