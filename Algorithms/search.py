import heapq
import inspect
import sys

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """
    def  __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))

def manhattanDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Method not implemented: %s at line %s of %s" % (method, line, fileName))
    sys.exit(1)

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of tuples, (successor, stepCost), 
        where 'successor' is a successor to the current
        state and 'stepCost' is the incremental cost of expanding to that successor.
        """
        raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        raiseNotDefined()


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.
    """
    
    if problem.isGoalState(problem.getStartState()):
        return []
    
    directions = []
    marked = []
    stack = Stack()
    stack.push(problem.getStartState())
    father = {}
    
    while not stack.isEmpty():
        current_state = stack.pop()
        if current_state in marked:
            continue
        marked.append(current_state)
        
        if problem.isGoalState(current_state):
            while current_state != problem.getStartState():
                 directions.append(father[current_state])
                 current_state = father[current_state][0]
            return directions[::-1]
        successors = problem.getSuccessors(current_state)
        
        for suc in successors:
            if suc[0] in marked:
                continue
            father[suc[0]] = (current_state , suc[1])
            stack.push(suc[0])
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    
    if problem.isGoalState(problem.getStartState()):
        return []
    
    directions = []
    marked = []
    queue = Queue()
    queue.push(problem.getStartState())
    father = {}
    
    while not queue.isEmpty():
        current_state = queue.pop()
        if current_state in marked:
            continue
        marked.append(current_state)
        
        if problem.isGoalState(current_state):
            while current_state != problem.getStartState():
                 directions.append(father[current_state])
                 current_state = father[current_state][0]
            return directions[::-1]
        successors = problem.getSuccessors(current_state)
        
        for suc in successors:
            if suc[0] in marked:
                continue
            father[suc[0]] = (current_state , suc[1])
            queue.push(suc[0])
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    if problem.isGoalState(problem.getStartState()):
        return []
    
    directions = []
    marked = []
    queue = PriorityQueue()
    queue.push(problem.getStartState(), 0)
    father = {}
    cost = {}
    cost[problem.getStartState()] = 0
    
    while not queue.isEmpty():
        current_state = queue.pop()
        if current_state in marked:
            continue
        marked.append(current_state)
        
        if problem.isGoalState(current_state):
            while current_state != problem.getStartState():
                 directions.append(father[current_state])
                 current_state = father[current_state][0]
            return directions[::-1]
        successors = problem.getSuccessors(current_state)
        
        for suc in successors:
            cost_suc = cost[current_state] + suc[1]
            if suc[0] not in cost or cost_suc < cost[suc[0]]:
                cost[suc[0]] = cost_suc
                father[suc[0]] = (current_state, suc[1])
                queue.push(suc[0], cost_suc)
    return []
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return []
    
    directions = []
    marked = []
    queue = PriorityQueue()
    queue.push(problem.getStartState(), 0)
    father = {}
    cost = {}
    cost[problem.getStartState()] = 0
    
    while not queue.isEmpty():
        current_state = queue.pop()
        if current_state in marked:
            continue
        marked.append(current_state)
        
        if problem.isGoalState(current_state):
            while current_state != problem.getStartState():
                 directions.append(father[current_state])
                 current_state = father[current_state][0]
            return directions[::-1]
        successors = problem.getSuccessors(current_state)
        
        for suc in successors:
            cost_suc = cost[current_state] + suc[1] + heuristic(suc[0], problem)
            if suc[0] not in cost or cost_suc < cost[suc[0]]:
                cost[suc[0]] = cost_suc - heuristic(suc[0], problem)
                father[suc[0]] = (current_state , suc[1])
                queue.push(suc[0], cost_suc)
    return []
