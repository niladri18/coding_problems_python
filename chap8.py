import sys
'''
Write a method to generate the nth Fibonacci number
'''
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:	
		f = fibonacci(n-1) + fibonacci(n-2)
		return f
		
		
print('Problem 8.1:')
print('')
n = 6
print(fibonacci(n))

'''
Write a method that returns all subsets of a set
'''
def allsubset(A):
	n = len(A)
	max_i = 1 << n
	subset = []
	for num in range(max_i):
		index = 0
		tmp = []
		while num > 0:
			if num&1 > 0:
				tmp.append(A[index])
			index += 1
			num = num >> 1
		subset.append(tmp)
	return subset
	
print('Problem 8.3:')
print('')	
A = list('abcd')
n = len(A)
S = allsubset(A)
for i in S:
	print(i)	
	
'''
Write a method to compute all permutations of a string
'''
def permutation(S):
	n = len(S)
	if n < 2:
		return S
	else:
		first = S[0]
		right = S[1:]
		ans = permutation(S[1:])

		tmp = []
		for word in ans:
			m = len(word)
			for i in range(m+1):
				t = word[:i] + first + word[i:]
				if t not in tmp:
					tmp.append(t)

		return tmp
		

print('Problem 8.4:')
print('Write a method to compute all permutations of a string')	
print('')
		
S = list('abba')
#S = 'abc'
ans = permutation(S)
print(ans, len(ans)) 

























	
