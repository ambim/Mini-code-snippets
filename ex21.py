#EXercise 21 Functions can return something 

def add (a, b):
	print "ADDING %d + %d" % (a,b)
	return a+b
	
def subtract (a, b): 
	print "SUBTRACTING %d - %d" % (a, b)
	return a-b
	
def multiply (a,b) : 
	print "MULTIPLYING %d * %d " % (a, b) 
	return a*b
	
def divide (a, b): 
	print "DIVIDING %d / %d" % (a, b) 
	return a/b
	
print "Let's do some math with just functions!" 
print "what's your age?" 
age =multiply(float(raw_input()), 2)  
print "so your age is... %d" % age  
height = subtract (78, 4) 
weight = multiply (90, 2) 
iq = divide (100,2) 

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq) 

print "the puzzle..." 

what = add(age, subtract (height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand? " 
