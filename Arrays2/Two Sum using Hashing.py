class Solution:
  def two_sum_exists(self, arr,target):
    mp={}
    for i,num in enumerate(arr):
      complement = target - num
      if complement in mp:
        return "Yes"
      mp[num] = i
    return "No"
if __name__ == "__main__":
  sol = Solution()
  arr = [2,6,5,8,11]
  target = 14
  result = sol.two_sum_exists(arr,target)
  print(result)