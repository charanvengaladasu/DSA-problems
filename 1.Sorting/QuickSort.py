'''
#for middle pivot element.
def quicksort(arr):
  if len(arr)<=1:
    return arr
  pivot = arr[len(arr) // 2]

  left = [x for x in arr if x < pivot]  
  right = [x for x in arr if x>pivot]
  middle= [x for x in arr if x==pivot]
  return quicksort(left) + middle + quicksort(right)
data = [1,21,12,41,24,13,7]
print(quicksort(data))

'''

#for 1st element as pivot.
def partition(arr, low, high):
  pivot = arr[low] #1st element as pivot
  left = low+1 #if not taken like this gets cpde stucks in infinite loop [captain and team example]
  right = high

  while True:
    # Move left pointer rightward
    while left <=right  and arr[left] <= pivot :
      left+=1
    # Move right pointer leftward
    while left <= right and arr[right] >= pivot :
      right-=1
    if left<=right:
      arr[left], arr[right] = arr[right],arr[left]
    else:
      break
    
    # Put pivot in its correct sorted position
  arr[low],arr[right]=arr[right],arr[low]
  return right

def quicksort(arr, low, high):
  if low<high: #base condition=This is the safety switch (base case). It stops the code when a sub-array has only 0 or 1 element left.
    pi = partition(arr, low, high)
    quicksort(arr, low, pi-1)
    quicksort(arr, pi+1, high)

data = [12,21,32,123,14,15]
quicksort(data, 0, len(data)-1)
print("the sorted array is:",data)