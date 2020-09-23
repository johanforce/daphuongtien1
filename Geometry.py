import math

def prob(n, p): 
  return (1-p)**(n-1)*p

def infoMeasure(n, p):
  Pr = prob(n, p)
  return - math.log2(Pr)

def sumProb(N, p):
  '''
    Trả về giá trị là tổng các xác xuất của symbol từ 1 đến N
    sum = p(1) + p(2) + .. + P(N) 
    sum = p^0*(1-p) + p^1*(1-p) + ... 
    sum = (1-p)*[1 + p + p^2 + ...] = (1-p)*1/(1-p) = 1
    khi N đủ lớn sum sẽ tiến gần đến 1
    ---
    Parameters:
    - N: int
      số symbol
    - p: float or int
      xác xuất mặt ngửa
    Return:
      sum: float
  '''
  sum = 0
  for i in range(1, N):
    sum += prob(i, p)
  return sum

def approxEntropy(N, p):
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
  for i in range(1, N):
    H += prob(i, p) * infoMeasure(i, p)
  return H

if __name__ == "__main__":
  """
    Test function
  """
  print('Prob of symbol 5: ', prob(5, 1/2))
  print('Amount of info of symbol 5: ', infoMeasure(5, 1/2))
  print('Total prob of 50 first symbol: ', sumProb(50, 1/2))
  print('Average amount of info of 50 first symbol: ', approxEntropy(50, 1/2))
