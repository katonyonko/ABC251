import io
import sys

_INPUT = """\
6
6 8
5 1
4 3
1 4
3 5
1 2
2 6
1 6
4 2
4 3
3 1
1 2
1 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import sys
  sys.setrecursionlimit(1000000)
  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  for i in range(M):
    u,v=map(int,input().split())
    u-=1; v-=1
    G[u].append(v)
    G[v].append(u)
  T1=[]
  used=[0]*N
  def rec(k):
    used[k]=1
    for v in G[k]:
      if used[v]!=1:
        T1.append((k,v))
        rec(v)
  rec(0)
  T2=[]
  used=[0]*N
  used[0]=1
  from collections import deque
  def bfs(G,s):
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if used[y]==0:
          used[y]=1
          dq.append(y)
          T2.append((x,y))
  bfs(G,0)
  for i in range(N-1):
    print(T1[i][0]+1,T1[i][1]+1)
  for i in range(N-1):
    print(T2[i][0]+1,T2[i][1]+1)