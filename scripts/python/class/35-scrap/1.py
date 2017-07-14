
''' 
a = "hai pradeep"
print a.count(' ')
print a.count('')
''' 

def get_word_count(t):
    print t
    return len(t.split(' '))

str = "Line1-ab cdef Line2-abc Line4-abcd";
print get_word_count(str)

mystr = "how are you"
print mystr

newlist = ""
for w in (mystr.split(' ')):
    #print w
    #print type(w)
    #print w[::-1].capitalize()
    newlist = newlist +  w[::-1].capitalize() + " "

print newlist



