import io
import sys

_INPUT = """\
6
6
12
1000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  W=int(input())
  A=[]
  for i in range(10**2):
    A.append(i+1)
    A.append((i+1)*10**2)
    A.append((i+1)*10**4)
  print(300)
  print(*A)