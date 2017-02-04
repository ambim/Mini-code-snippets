from sys import argv 

script, user_name = argv 

prompt = 'Answer: '
response = "Thanks for that response %s!" % user_name

print "Thanks for logging on %s" % user_name
print "How long have you been programming, %s?" % user_name
prog = raw_input(prompt)

print response 
print "What is this shit you're watching?" 
film = raw_input(prompt)

print response 
