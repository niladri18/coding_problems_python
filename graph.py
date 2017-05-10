import sys

class Dgraph:
	def __init__(self):
		self.item = {}
	
	def addVertex(self,u):
		self.item[u] = []
	def addEdge(self,u,v):
		if u not in self.item.keys():
			self.item[u] = []
		if v not in self.item.keys():
			self.item[v] = []
		self.item[u].append(v)
	def show(self):
		for i,j in self.item.items():
			print(i,j)
	def getEdge(self,u):
		if u in self.item.keys():
			return self.item[u]
		else:
			return None		
			
			
			
					


	
