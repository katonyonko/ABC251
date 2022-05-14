import io
import sys

_INPUT = """\
6
5
2 5 3 2 5
20
29 27 79 27 30 4 93 89 44 88 70 75 96 3 78 39 97 12 53 62
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  dp=[A[0],10**100]
  for i in range(N-1):
    tmp=[min(dp[0],dp[1])+A[i+1], dp[0]]
    dp=tmp.copy()
  ans=min(dp)
  dp=[A[-1],10**100]
  for i in range(N-1):
    tmp=[min(dp[0],dp[1])+A[i], dp[0]]
    dp=tmp.copy()
  ans=min(ans,min(dp))
  print(ans)