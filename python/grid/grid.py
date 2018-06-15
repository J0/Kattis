# Let us first obtain all the inputs
from collections import deque
_list = [int(x) for x in input().split()]
ROWS = _list[0]
COLUMNS = _list[1]
GRID2D = [[x for x in range(COLUMNS)] for y in range(ROWS)]
# Now, populate the array
for z in range(ROWS):
    row = [int(x) for x in input()]
    GRID2D[z] = row


class Edge:
    def __init__(self, weight, _from, _to):
        self.weight = None
        self._from = _from
        self._to = _to

    def get_predecessor(self):
        return self.previous


class Vertex:
    def __init__(self, row, column, pre):
        self._id = row * COLUMNS + column
        self.row = row
        self.column = column
        self.magnitude = GRID2D[row][column]
        self.pre = pre

    def get_vertex(self):
        return self.id

    def get_adjacent(self):
        adj_list = []

        if self.row + self.magnitude < ROWS:
            adj_list.append(Vertex(self.row + self.magnitude, self.column, self._id))
        if self.row - self.magnitude >= 0 :
            adj_list.append(Vertex(self.row - self.magnitude, self.column, self._id))
        if self.column + self.magnitude < COLUMNS:
            adj_list.append(Vertex(self.row, self.column + self.magnitude, self._id))
        if self.column - self.magnitude >= 0:
            adj_list.append(Vertex(self.row, self.column - self.magnitude, self._id))
        # Check the position after adding the relevant magnitude
        return adj_list

    def __str__(self):
        return "This vertex has %s id and is in %s row %s column with %s weight. It's predecessor is %s" % (self._id, self.row, self.column, self.magnitude,self.pre)


def breadth_first_search(start_vertex, target, num_vertices):
    """
    :param starting -- This is the vertex where we commence bfs
    :target target -- This is the vertex which we want to find the shortest path to
    """
    queue = deque()
    visited = [False] * num_vertices
    path = [-1] * num_vertices
    queue.append(start_vertex)
    visited[start_vertex._id] = True
    # Append the starting vertex into the queue
    # While the queue is not empty
    while queue:
        vertex = queue.popleft()
        # print("This is the first vertex to be popped %s" %vertex)
        if vertex._id == target._id:
            return construct_path(path)
        else:
            # If not visited before
            for vert in vertex.get_adjacent():
                if not visited[vert._id]:
                    queue.append(vert)
                    path[vert._id] = vert.pre
                    visited[vert._id] = True

    # If you can still move within the grid, continue adding vertices and
    # If you reach the target, break out of the loop
    return -1

# Produce a backtrace of the actions taken to find the goal node, using the recorded meta dictionary
def construct_path( path):
    """
    :param path   List of vertices containing the path
    """
    action_state = []
    _pre = -1
    while path[_pre] != -1:
        _pre = path[_pre]
        action_state.append(_pre)
    return len(action_state)

start_vertex = Vertex(0,0, -1)
# print(start_vertex)
end_id = ROWS * COLUMNS - 1
end_vertex = Vertex(ROWS - 1, COLUMNS -1, None)
# print(end_vertex)
num_vertices = ROWS * COLUMNS
print(breadth_first_search(start_vertex, end_vertex, num_vertices))
