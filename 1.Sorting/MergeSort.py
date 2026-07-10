def merge_sort(arr):
  if len(arr)>1: #this is an base case for recursion and if we take [] or [4] like this, by further dividing it will divide into same again and loops forever.
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half= arr[mid:]

    #Recursive calls
    merge_sort(left_half)
    merge_sort(right_half)

    i=j=k=0 

    while i <len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        arr[k] = left_half[i]
        i+=1   #moving the pointer to next value in left_half
      else:
        arr[k] = right_half[j]
        j+=1  #moving the pointer to next value in right_half
      k+=1

    #Checking if any element was left in either half
    while i < len(left_half):
      arr[k] = left_half[i]
      i+=1
      k+=1
    while j < len(right_half):
      arr[k] = right_half[j]
      j+=1
      k+=1
data = [12,34,24,56,22,4,31]
merge_sort(data)
print("sorted_array:",data)