import sys

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	def add(self,data):
		if self.next:
			self.next.add(data)
		else:
			self.next = Node(data)
		pass
	def show(self):
		current = self
		while current:
			print(current.data, end = ',')
			current = current.next
		print('')	
		pass
	def setdata(self,data):
		self.data = data	
		 	
		
class Queue:
	def __init__(self):
		self.item = None
		self.size = 0
		
	def add(self,data):
		if self.item:
			self.item.add(data)
		else:
			self.item = Node(data)
	def dqueue(self):
		if self.item:
			if self.item.next:
				p = self.item.data
				self.item.data = self.item.next.data
				self.item.next = self.item.next.next
			else:
				p = self.item.data # Delete the last node
				self.item = None
			return p
		else:
			return None
			
	def getdata(self):
		return self.item.data
	def getnext(self):
		return self.item.next
	def setdata(self,data):
		self.item.setdata(data)		
	def show(self):
		if self.item:
			self.item.show()
		else:
			print('Empty List!')			
	def isEmpty(self):
		return self.item == None
			
					
					
					
					
