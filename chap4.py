import sys
import bstv1 as bst
import graph as gp
import pdb

def solution1(T):
	'''
	Problem 4.1:
	Implement a function to check if a tree is balanced. For the purposes of this question, 
	a balanced tree is defined to be a tree such that no two leaf nodes differ in distance 
	from the root by more than one
	'''
	ans = T.l2n() #Calculate the different leaf to node paths
	l = []
	for i in ans:
		l.append(len(i)) # store lengths of different leaf to node paths
	flag = max(l)-min(l)
	if flag > 1:
		return False
	else:
		return True
				
	
def solution2(G,start,end):
	'''
	Problem 4.2
	Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
	'''
	stack = [start]
	xp = []
	flag = False
	while stack and not flag:
		u = stack.pop()
		for i in G.getEdge(u):
			flag = (i == end)
			if flag:
				break
			if i not in xp:
				xp.append(i)
				stack.append(i)
	return flag				


def solution3(x,T):
	'''
	Problem 4.3:
	Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
	'''
	n = len(x)
	if n < 2:
		T.insert(x[0])
	else:
		left = x[:n//2]
		right = x[n//2+1:]
		T.insert(x[n//2])
		if left:
			solution3(left,T)
		if right:
			solution3(right,T)
		
		
	return T	

def solution4(T):
	'''
	Problem 4.4:
	Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth 
	(eg, if you have a tree with depth D, you’ll have D linked lists).
	'''
	level = {}
	dist = {}
	start = T.getRoot()# Store the root node
	dist[start] = 0
	d = dist[start]
	level[d] = [start.getdata()]
	
	q = [start]
	xp = [start]
	while q:
		u = q.pop(0)
		left = u.getLeft()
		right = u.getRight()
		#pdb.set_trace()
		if (left not in xp) and left:
			d = dist[u] + 1
			dist[left] = d
			if d not in level.keys():
				level[d] = []
			level[d].append(left.getdata())
			xp.append(left)
			q.append(left) 
		if (right not in xp) and right:
			d = dist[u] + 1
			dist[right] = d
			if d not in level.keys():
				level[d] = []
			level[d].append(right.getdata())
			xp.append(right)
			q.append(right)
	return level
	

def solution6(T,a,b):
	'''
	Problem 4.6:
	Design an algorithm and write code to find the first common ancestor of 
	two nodes in a binary tree. Avoid storing additional nodes in a data structure
	'''
	root = T.getdata()
	#print(root,a,b)
	if a == root:
		return root
	if b == root:
		return root
	if a < root and b > root:
		return root
	elif a > root and b < root:
		return root
	elif a > root and b > root:
		subT = T.getRight()
		
	elif a < root and b < root:
		subT = T.getLeft()
		
	return solution6(subT,a,b)	

'''
Problem 4.8:
You are given a binary tree in which each node contains a value. 
Design an algorithm to print all paths which sum up to that value. 
Note that it can be any path in the tree - it does not have to start at the root
'''

	
def pathsum(node,s,finalsum,xp):
	root = node.getdata()
	s += root
	xp.append(root)
	if s == finalsum:
		print(xp)
		xp.pop()
	else:
		if node.getLeft():
			left = node.getLeft()
			pathsum(left,s,finalsum,xp)
		if node.getRight():
			right = node.getRight()
			pathsum(right, s, finalsum, xp)
		xp.pop()
			

			
def solution8(node,finalsum):
	if node.getLeft():
		solution8(node.getLeft(),finalsum)
	pathsum(node,0,finalsum,[])
	if node.getRight():
		solution8(node.getRight(),finalsum)
	
		
		
	
x = [8,2,5,6,17,14,4]	
T = bst.BST()
#Construct the tree
for i in x:
	T.insert(i)



print('Problem 4.1:')
flag = solution1(T)	
print(flag)
print('')	


print('Problem 4.2:')
x = [ ('a','b'), ('a','c'), ('a','d'), ('c','b'),('c','e'),('d','c'),('d','e'),('e','f') ]
G = gp.Dgraph()
for t in x:
	G.addEdge( t[0], t[1] )
	
ans = solution2(G,'a','b')
print(ans)	

print('Problem 4.3:')
x = [-2,-1, 1, 3,4,5,6,7,8,9,10]
T = bst.BST()
T = solution3(x,T)
ans = T.l2n()
for i in ans:
	print(i)
	
print('Problem 4.4:')
level = solution4(T)
print(level)
	
print('Problem 4.6:')
a = 10
b = 8
rootnode = T.getRoot()
ans = solution6(rootnode, a,b)
print(ans)

print('Problem 4.8:')
node = T.getRoot()
solution8(node,18)



