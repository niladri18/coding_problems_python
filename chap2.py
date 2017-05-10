import sys
import pdb
import listv1 as lst

def add(a,b):
	c = lst.Queue()
	while not a.isEmpty() and not b.isEmpty():
		tmp = a.getdata() + b.getdata()
		s = tmp%10
		carry = tmp//10
		c.add(s)
		a.dqueue()
		b.dqueue()
		if not a.isEmpty():
			num = a.getdata()
			a.setdata(num+carry)
		elif not b.isEmpty():
			num = b.getdata()
			b.setdata(num+carry)
	#pdb.set_trace()
	while not a.isEmpty():
		tmp = a.getdata()
		s = tmp%10
		carry = tmp//10
		c.add(s)
		a.dqueue()
		if not a.isEmpty():
			num = a.getdata()
			a.setdata(num + carry)
	while not b.isEmpty():
		tmp = b.getdata() + carry
		s = tmp%10
		carry = tmp//10
		c.add(s)
		b.dqueue()
		if not b.isEmpty():
			num = b.getdata()
			b.setdata(num+carry)
	if carry > 0:	
		c.add(carry)		
	return c			
	

x = [8,9,1,3,5,7,2,11]
Q = lst.Queue()
for i in x:
	Q.add(i)
	
Q.show()
while not Q.isEmpty():
	#pdb.set_trace()
	print(Q.dqueue())
	
x = [3,1,5,1]
y = [5,9,9,9]
a = lst.Queue()
b = lst.Queue()
for i in x:
	a.add(i)
for i in y:
	b.add(i)

a.show()
b.show()	
c = add(a,b)
c.show()		



	
