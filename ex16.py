from sys import argv 

script, filename = argv 

print "We are going to erase %r" % filename 
print "If you dont want that hit CTRL-C (^c)."
print "If you do want that hit Return" 

raw_input("?")

print "opening the file..."
target = open(filename,'w')

print "Truncating the file... goodbye!" 
target.truncate()

print "Now i'm going to ask you for three lines" 

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "now im going to write those line's to a file" 

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

txt = open(filename) 
print txt.read()


print "and finally we close it" 
target.close()
print "Close successful" 

