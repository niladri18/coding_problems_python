import sys
import pdb

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	def insert(self,data):
		if data < self.data:
			if self.left:
				self.left.insert(data)
			else:
				self.left = Node(data)
		else:
			if self.right:
				self.right.insert(data)
			else:
				self.right = Node(data)
	def isleaf(self):
		flag = (self.left == None) and (self.right == None)
		return flag
		
	def l2n(self,xp):
		#pdb.set_trace()
		xp.append(self.data)
		if self.isleaf():
			#print(xp)
			yield xp
			xp.pop()
		else:
			if self.left:
				#self.left.l2n(xp)
				yield from self.left.l2n(xp)
			if self.right:
				#self.right.l2n(xp)
				yield from self.right.l2n(xp)
			xp.pop()
	def getdata(self):
		return self.data
	def getLeft(self):
		return self.left
	def getRight(self):
		return self.right	

class BST:
	def __init__(self):
		self.item = None
		self.size = 0
	def insert(self,data):
		self.size += 1
		if self.item:
			self.item.insert(data)
		else:
			self.item = Node(data)
	def show(self):
		if self.item:
			self.item.show()
		else:
			return None
			
	def getRoot(self):
		if self.item:
			return self.item
	def getLeft(self):
		#if self.item.getleft():
		return self.item.getLeft()
	def getRight(self):
		#if self.item.getright():
		return self.item.getRight()
						
	def l2n(self):
		#pdb.set_trace()
		if self.item:
			xp = []
			yield from self.item.l2n(xp)
		
