#arr=[1,2,3,4,5,5,6]
def isSorted(arr,n):
  for i in range(n-1):
    if arr[i+1] < arr[i]:
      return False
    return True

arr = [1,2,3,4,5,5,6]
n = len(arr)
ans = isSorted(arr,n)
if ans:
  print("true")
else:
  print("false")