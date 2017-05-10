import sys
'''
Problem 5.1
You are given two 32-bit numbers, N and M, and two bit positions, i and j. 
Write a method to set all bits between i and j in N equal to M 
(e.g., M becomes a substring of N located at i and starting at j).
'''


x = int('101011',2)
y = int('1000111100000',2)
j = 2
i = 7

#All 1's
max_i = ~0

#All 1's from left to i
left = max_i -((1 << i)-1)

#All 1's to the right of j
right = (1<<j) - 1

mask = left|right
movex = x << j
print(bin(movex))
print(bin((mask&y)|movex))

'''
Given a (decimal - e.g. 3.72) number that is passed in as a string, 
print the binary representation. If the number can not be represented 
accurately in binary, print “ERROR”
'''
x = '3.72'
x = '0.25'
x = x.split('.')
print(x)
n = int(x[0])
intpart = ''
while n > 0:
	bit = int(n%2)
	#print(str(bit))
	n = n//2 
	intpart += str(bit)


d = float('.'+x[1])
#print(d)
decpart = ''
while d > 0:
	if len(x[1]) > 32:
		print('ERROR:')
		break
	if d==1:
		decpart += str(d)
		break
	r = d*2
	if r >= 1:
		decpart += str(1)
		d = r-1
	else:
		decpart += str(0)
		d = r
		
	

print(intpart+'.'+decpart)	










