import operator as op
import sys
sys.setrecursionlimit(10000)

cache = {}

def funk(n, r, norm):
  if (n,r) in cache:
    return cache[(n,r)]
  if r==0:
    cache[(n,r)] = 1
  elif r==n:
    cache[(n,r)] = 1
  else:
    cache[(n,r)] = (funk(n-1, r, norm) + funk(n-1, r-1, norm)) % norm
  return cache[(n,r)]

def funk(n, r, norm):
  for level in xrange(n+1):
      
      cache[(n,r)] = (funk(n-1, r, norm) + funk(n-1, r-1, norm)) % norm
  return cache[(n,r)]

#n = input()
n, k = map(int, raw_input().split(' '))
print funk(n-1, k-1, 10**9+7)
