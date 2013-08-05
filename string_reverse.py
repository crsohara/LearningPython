'''
Created on Aug 5, 2013

@author: seriousbuns
'''
string = list(raw_input("Enter string to reverse: "))
string2 = list()

print "you entered: ", ''.join(string)

for n in reversed(xrange(len(string))):
    string2.append(string[n])

    
print "reversed: ", string2