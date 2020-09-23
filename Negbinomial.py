import math

def nCk(n, k):
  """
    k Combination of n = [(n-(k-1))*(n-(k-2))*..*(n-1)*n]/k! = n-k Combination of n
  """
  if k > n :
    return 0
  res = 1
  pivot = min(k, n-k)
  for i in range (1, pivot + 1):
    res *= (n-i+1)/i
  return round(res)

def prob(n, p, r):
  '''
  Trả về giá trị là xác xuất của symbol n (hay k) với k = {0,1,2..}
  trên tập symbol X = {r, r + 1, r + 2, ...}
  Xk = r + k
  ---
  Parameters:
  - n: int
    symbol
  - p: float or int
    xác xuất mặt ngửa
  - r: int
    số lần xuất hiện mặt ngửa
  Return:
    nCk(n+r-1, n)*(p**r)*((1-p)**n)
  '''
  return nCk(n+r-1, n)*(p**r)*((1-p)**n)

def infoMeasure(n, p, r):
  Pr = prob(n, p, r)
  return - math.log2(Pr)

def sumProb(N, p, r):
  '''
    Trả về giá trị là tổng các xác xuất của các symbol {r, r+1, r+2, ..., r+N}
    sum = p(1) + p(2) + .. + P(N) 
    khi N đủ lớn sum sẽ tiến gần đến 1
    ---
    Parameters:
    - N: int
      số symbol
    - p: float or int
      xác xuất mặt ngửa
    - r: int
      số lần xuất hiện mặt ngửa
    Return:
      sum: float
  '''
  sum = 0
  for i in range(0, N):
    sum += prob(i, p, r)
  return sum

def approxEntropy(N, p, r):
  '''
    Trả về giá trị trung bình lượng tin của các symbol {1,..,N}
    H = -p(1)*log(p1) - p(2)*log(p2) + .. + -p(N)*log(p(N)) 
    khi N đủ lớn H sẽ tiến gần đến entropy của nguồn tin
    ---
    Parameters:
    - N: int
      số symbol
    - p: float or int
      xác xuất mặt ngửa
    Return:
      H: float
  '''
  H = 0
  for i in range(0, N):
    H += prob(i, p, r) * infoMeasure(i, p, r)
  return H

if __name__ == "__main__":
  """
    Test function
  """
  print('5 Combination of 15: ', nCk(15, 5))
  print('Prob of symbol 5: ', prob(5, 1/2, 15))
  print('Amount of info of symbol 5: ', infoMeasure(5, 1/2, 15))
  print('Total prob of r = 15: ', sumProb(50, 1/2, 15))
  print('Average amount of info of r = 15: ', approxEntropy(50, 1/2, 15))
