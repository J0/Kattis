import heapq
n = 1 
m = 1
q = 1 
s = 1
class Vertex:
  def __init__(self, node):
    self.id = node
    self.adjacent = {}
    self.distance = 10000000
    self.visited = False
    self.previous = None
  def add_neighbour(self, neighbour, weight=0):
    self.adjacent[neighbour] = weight
  def __str__(self):
    return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])




while(1):
  n, m, q, s = input().split()
  print("%s %s %s %s" %(n, m, q, s))
  if(n == "0" and m == "0" and q == "0" and s == "0"):
    break
  for counter in range(int(m)):
    u, v, w = input().split()
    adj_list = [[0 for x in range(int(n))] for y in range(int(n))]
    print(adj_list)
    print("%s %s %s" %(u, v, w))
  for query in range(int(q)):
    destination = input()
    print(destination)




def dijkstra(adj_list, start_node, end_node):
  
  distance[start_node] = 0
  

  pass


def relax():
  pass

