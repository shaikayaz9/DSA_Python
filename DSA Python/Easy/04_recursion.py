def n_func(k):
  if(k> 0):
    result = k + n_func(k - 1)
    print(result)
  else:
    result = 0
  return result
    
print("\n\nrecursion Example results")

n_func(5)