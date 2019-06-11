# list as Queue

from collections import deque
q=deque([1,2,3,4,5])
print(q) 
q.append(6)
print(q)
print(q.popleft())
print(q.appendleft(7))
print(q.pop())