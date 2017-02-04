#exercise19 extra functions 

def myFunction (drinks, days, road):
	print "I tend to enjoy %d drinks at %d o'clock" % (drinks, days)
	print "In fact, I rarely venture outside the M%d" % road 
	
myFunction (2, 7, 25) 

print "\n"



def myFunc2 (piles_per_km, site_perimeter):
	totalPiles = piles_per_km * site_perimeter
	print "total number of piles required: %d" % totalPiles
	
piles_per_km = 450/9
site_perimeter = 6+4+7+1+3

myFunc2 (piles_per_km, site_perimeter)