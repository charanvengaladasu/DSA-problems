# Variant 1: Check if two numbers sum to target using two-pointer approach. if yes return "Yes" if no return "No"

class Solution:
  def two_sum_exists(self,arr,target):
    n=len(arr)
    nums_with_index = [(num,idx) for idx, num in enumerate(arr)]  
    nums_with_index.sort(key=lambda x:x[0])
    left = 0
    right = n-1
    while left < right:
      current_sum = nums_with_index[left][0] + nums_with_index[right][0]
      if current_sum == target:
        return "Yes"
      elif current_sum < target:
        left += 1
      else:
        right -= 1
    return "No"
    
if __name__ == "__main__":
  sol = Solution()
  arr = [2,6,5,8,11]
  target = 14
  print(sol.two_sum_exists(arr,target))

# TC is O(NlogN)
# SC is O(N)
#Hashing is more optimal than this (two pointers)