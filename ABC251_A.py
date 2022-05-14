import io
import sys

_INPUT = """\
6
abc
zz
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  print(S*(6//len(S)))