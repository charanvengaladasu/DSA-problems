class Solution:
  def longestSubarray(self,nums,k):
    n=len(nums)
    maxLen = 0
    left,right = 0,0
    sum = nums[0]

    while(right < n):
      while left<=right and sum > k:
        sum -= nums[left]
        left+=1
      if sum == k:
        maxLen = max(maxLen, right-left+1)
      right +=1
      if right < n:
        sum += nums[right]
    return maxLen


nums = [10,5,2,7,1,9]
k=15
sol = Solution()
ans = sol.longestSubarray(nums,k)
print("The length of the subarray having sum k is:",ans)