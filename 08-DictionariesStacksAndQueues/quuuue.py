from collections import deque

stock = []

stock.insert(0,131.1)
stock.insert(0,132.12)
stock.insert(0,134)
stock.pop()
print(stock)

q = deque()
q.appendleft(5)
q.appendleft(7)
q.appendleft(10)
q.pop()
