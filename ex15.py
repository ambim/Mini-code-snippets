from sys import argv 
script, filename = argv 

# using the argv to enter filename in cmd line 
txt = open(filename)


print "Here's your file %r:" % filename 
print txt.read()

print "Type the file name again: "
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()

txt.close()
txt_again.close()
print "txt and txt_again files are now closed"




