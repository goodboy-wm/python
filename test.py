
from collections import deque


buff = ["a","b"]
a = ["c","d"]

queue = deque()
queue += buff

a.append("m")

buff += a

print(buff)