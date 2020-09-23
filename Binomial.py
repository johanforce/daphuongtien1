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

def prob(n, p, N):
  return nCk(N, n)*(p**n)*((1-p)**(N-n))

def infoMeasure(n, p, N):
  Pr = prob(n, p, N)
  return - math.log2(Pr)

def sumProb(N, p):
  '''
    Trả về giá trị là tổng tất cả các xác xuất của các symbol {0,..,N}
    sum = p(0) + p(1) + .. + P(N) 
    sum xấp xỉ 1
    ---
    Parameters:
    - N: int
      số đồng xu
    - p: float or int
      xác xuất mặt ngửa
    Return:
      sum: float
  '''
  sum = 0
  for i in range(0, N):
    sum += prob(i, p, N)
  return sum

def approxEntropy(N, p):
  '''
    Trả về giá trị trung bình lượng tin của các symbol {0,..,N}
    H = -p(0)*log(p0) - p(2)*log(p2) + .. + -p(N)*log(p(N)) 
    khi N đủ lớn H sẽ tiến gần đến entropy của nguồn tin
    ---
    Parameters:
    - N: int
      số đồng xu
    - p: float or int
      xác xuất mặt ngửa
    Return:
      H: float
  '''
  H = 0
  for i in range(0, N):
    H += prob(i, p, N) * infoMeasure(i, p, N)
  return H

if __name__ == "__main__":
  """
    Test function
  """
  print('5 Combination of 50: ', nCk(50, 5))
  print('Prob of symbol 5: ', prob(5, 1/2, 50))
  print('Amount of info of symbol 5: ', infoMeasure(5, 1/2, 50))
  print('Total prob of N = 50: ', sumProb(50, 1/2))
  print('Average amount of info of N = 50: ', approxEntropy(50, 1/2))
