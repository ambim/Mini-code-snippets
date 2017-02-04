#exercise 17 more files 

from sys import argv 
from os.path import exists

script, from_file, to_file = argv 

print "Copying from %s to %s" % (from_file, to_file) 

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
open_to = open(to_file)
open_to.truncate()


print "Ready, hit RETURN to continue, CTRL-C to abort." 

raw_input()

#deleting any text that might be in the test file 
to_file.truncate()
out_file = open (to_file, 'w')
out_file.write(indata) 

print "Alright, all done." 

out_file.close()
in_file.close()

