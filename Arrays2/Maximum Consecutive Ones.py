#arr = [0,1,1,1,0,0,1,1,0,0,1,1,1,1]

class Solution:
  def findMaxConsecutiveOnes(self, nums):
    count = 0
    maxi = 0

    for i in range(n):
      if nums[i] == 1:
        count +=1
      else:
        count = 0
      maxi = max(maxi,count)
    return maxi
nums =[0,1,1,1,0,0,1,1,0,0,1,1,1,1]
n=len(nums)
obj = Solution()
ans = obj.findMaxConsecutiveOnes(nums)
print("The Max Consecutive 1's are :",ans)