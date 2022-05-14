import io
import sys

_INPUT = """\
6
3
aaa 10
bbb 20
aaa 30
5
aaa 9
bbb 10
ccc 10
ddd 10
bbb 11
10
bb 3
ba 1
aa 4
bb 1
ba 5
aa 9
aa 2
ab 6
bb 5
ab 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  st=[input().split() for _ in range(N)]
  original={}
  for i in range(N):
    if st[i][0] not in original: original[st[i][0]]=int(st[i][1])
  t=max([original[k] for k in original])
  used=set()
  for i in range(N):
    if st[i][0] not in used:
      used.add(st[i][0])
      if original[st[i][0]]==t:
        print(i+1)
        break