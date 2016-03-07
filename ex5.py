name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 # lbs
eyes ='Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." %name
print "He's %d inches tall." %height
print "He's %d pounds heavy" % weight
print "Actually thats not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky
print "If I add %r, %d and %d I get %d." %(
	age, height, weight, age + height + weight)