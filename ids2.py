
from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
from queue import Queue
from copy import deepcopy
from random import randint

class TilePuzzle:
	def __init__(self,size):
		self.size=size
		self.puzzle=[]
		self.zero=(0,0)
		self.moves=["U","D","L","R"]
		count=1
		for i in range(0,size):
			self.puzzle.append([])
			for j in range(0,size):
				self.puzzle[i].append(count)
				count+=1
		self.puzzle[size-1][size-1]=0
		self.zero=(size-1,size-1)

	def readPuzzle(self,string):
		a=string.split(" ")
		count=0
		for i in range(0,self.size):
			for j in range(0,self.size):
				if int(a[count])==0:
					self.zero=(i,j)
				self.puzzle[i][j]=int(a[count])
				count+=1

	def checkPuzzle(self):
		count=1
		for i in range(0,self.size):
			for j in range(0,self.size):
				if self.puzzle[i][j]!=(count%(self.size*self.size)):
					return False
				count+=1
		return True

	
	def swap((self,(x1,y1)),(x2,y2)):
		temp=self.puzzle[x1][y1]
		self.puzzle[x1][y1]=self.puzzle[x2][y2]
		self.puzzle[x2][y2]=temp

	def up(self):
		if (self.zero[0]!=0):
			self.swap((self.zero[0]-1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]-1,self.zero[1])
	def down(self):
		if (self.zero[0]!=self.size-1):
			self.swap((self.zero[0]+1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]+1,self.zero[1])

	def left(self):
		if (self.zero[1]!=0):
			self.swap((self.zero[0],self.zero[1]-1),self.zero)
			self.zero=(self.zero[0],self.zero[1]-1)


	def right(self):
		if (self.zero[1]!=self.size-1):
			self.swap((self.zero[0],self.zero[1]+1),self.zero)
			self.zero=(self.zero[0],self.zero[1]+1)
	
	def printPuzzle(self):
		for i in range(0,self.size):
			for j in range(0,self.size):
				print self.puzzle[i][j],
			print ""
			#print 

	def doMove(self,move):
		if move=="U":
			self.up()
		if move=="D":
			self.down()
		if move=="L":
			self.left()
		if move=="R":
			self.right()
	
	def permute(self,numPerm):
		for i in range(0,numPerm):
			self.doMove(self.moves[randint(0,3)])
	
	def parseMoveSequence(self,string):
		for m in string:
			self.doMove(m)

class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        self.depth = 0
        if parent is None:
            self.depth = 0
            self.moves = move
        else:
            self.depth = parent.depth+1
            self.moves = parent.moves + move

    def goalState(self):
        return self.state.checkPuzzle()


    def succ(self):
        succs = Queue()
        for m in self.state.moves:
            p = deepcopy(self.state)
            p.doMove(m)
            if p.zero is not self.state.zero:
                succs.put(Node(p, self, m))
        return succs




class Search:


    def __init__(self, puzzle):
        self.start = node.Node(puzzle)

  
   
    def iterativeDeepening(self):
        depth = 0
        result = None
        while result == None:
            result = self.depthLimited(depth)
            depth +=1
        return result

    def depthLimited(self, depth):
        leaves = LifoQueue()
        leaves.put(self.start)
        while True:
            if leaves.empty():
                return None
            actual = leaves.get()
            if actual.goalState():
                return actual
            elif actual.depth is not depth:
                succ = actual.succ()
                while not succ.empty():
                    leaves.put(succ.get())

t=TilePuzzle(8)
t.permute(10)
t.printPuzzle()
s=Search(t)
print ("Considering Iterative Deepening Search:", s.iterativeDeepening())

    
  