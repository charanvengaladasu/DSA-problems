def insertion_sort(arr):
  n=len(arr)
  for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and key <arr[j]:
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=key
  return arr
data=[14,9,15,12,6,8,13]
insertion_sort(data)
print('Sorting through insertion sort:',data)