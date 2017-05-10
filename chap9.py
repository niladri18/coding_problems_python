import sys
'''
Write a method to sort an array of strings so that all the anagrams are next to each other
'''
class Word:
	def __init__(self,word,index):
		self.word = word
		self.index = index
		
	def sortword(self):
		tmp = sorted(self.word)
		tmp = ''.join(tmp)
		newword = Word(tmp,self.index)
		return newword

		
print('')
print('Problem 9.2:')
print('')

x = ['pqrs','acbd','tuv','abcd','aabc','prqs']

n = len(x)
#word_list = []
sort_list = []
for i in range(n):
	word = Word(x[i],i)
	#word_list.append(word)
	sort_list.append(word.sortword())
	
sort_list = sorted(sort_list,key = lambda t:t.word)
for t in sort_list:
	print(x[t.index])
	 	
'''
Given  a  sorted  array  of  n  integers  that  has  been  rotated  an  unknown  number  of 
times, give an O(log n) algorithm that finds an element in the array
You may assume that the array was originally sorted in increasing order.
'''	 	

def search(A,x):
	n = len(A)
	m = n//2
	l = 0
	r = n-1
	while l < r:
		m = (l + r)//2
		if x == A[m]:
			return m
		elif x == A[r]:
			return r
		elif A[l] < A[m]: # Left is sorted
			if x < A[m]:
				r = m-1
			else:
				l = m+1
		elif A[r] > A[m]: # Right is sorted
			if x < A[r]:
				l = m+1
			else:
				r = m-1
	return -1
	
print('')
print('Problem 9.3:')
print('')
	
A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
x = 15
print(search(A,x))

'''
A circus is designing a tower routine consisting of people standing atop one another’s shoulders
  For practical and aesthetic reasons, each person must be both shorter 
  and lighter than the person below him or her
  Given the heights and weights of each person in the circus, 
  write a method to compute the largest possible number of people in such a tower
'''

print('')
print('Problem 9.7:')
print('')

class person:
	def __init__(self,w,h):
		self.weight = w
		self.height = h
		
		
inp = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]								

n = len(inp)
person_list = []

for i in range(n):
	p = person(inp[i][0],inp[i][1])			
	person_list.append(p)

#Sort the list by height first	
sort_h = sorted(person_list, key =  lambda t: t.height)

w0 = sort_h[0].weight
final_list1 = [sort_h[0]]		
for x in sort_h:
	if x.weight > w0:
		final_list1.append(x)

n1 = len(final_list1)					 


# Then sort by weight
sort_w = sorted(person_list, key = lambda t: t.weight)
h0 = sort_w[0].height
final_list2 = [sort_w[0]]
for x in sort_w:
	if x.height > h0:
		final_list2.append(x)
		
n2 = len(final_list2)

# find which list is longer
if n1 > n2:
	final_list = final_list1
else:
	final_list = final_list2
							
for x in final_list:
	print(x.weight,x.height)
	
print(len(final_list))	

'''
Given a sorted array of strings which is interspersed with empty strings, write a method to 
find the location of a given string
'''
print('')
print('Problem 9.5:')
print('')

def find(A,x):
	n = len(A)
	l = 0
	r = n-1
	while l < r:
		m = (l+r)//2
		if x == A[m]:
			return m
		# if hits a spacebar
		if A[m] == '':
			t = A[m]
			c = m 
			# move to right to find the next non-empty entry
			while t == '': 
				c += 1
				t = A[c]
				
			# now search in the right array
			if x == A[c]:
				return c
			elif x > t:
				l = c+1
			else:
				r = m
		# if hits a word		
		else:
			if x > A[m]:
				l = m+1
			else:
				r = m
	return -1
				
		
		

inp = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '','um']
x =  'pray'

print(find(inp,x))




















				
				
				
				
				
				
				
				
				
				
				 
