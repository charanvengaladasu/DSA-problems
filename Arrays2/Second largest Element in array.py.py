def secondSmallest(arr,n):
  if n < 2:
    return -1
  small = float('inf')
  s_small = float('inf')

  for i in range(n):
    if arr[i]<small:
      s_small=small
      small=arr[i]
    elif arr[i]<s_small and arr[i] != small:
      s_small = arr[i]
  return s_small

def secondLargest(arr,n):
  if n<2:
    return -1
  
  large=float('-inf')
  s_large=float('-inf')
  for i in range(n):
    if arr[i]>large:
      s_large=large
      large=arr[i]
    elif arr[i]>s_large and arr[i] != large:
      s_large=arr[i]
  return s_large


if __name__ == "__main__":
  arr=[1,2,3,4,7,7,5]
  n=len(arr)

  sS=secondSmallest(arr,n)
  sL=secondLargest(arr,n)
  print(f"Second Largest is {sL}")
  print(f"Second Smallest is {sS}")