#!/usr/bin/python
class Person:
    # Constructor    
    def __init__(self,pos):
        self.pos = pos
        self.alive = 1
    # Destructor
    def __del__(self):
        print "We're done!"
    # informal string representation of an object. 
    def __str__(self):
        return "Person #%d, %s" % (self.pos, self.alive)
    
    # Creates a chain of linked people
    # Returns the last one in the chain
    def createChain(self,n):
        if n>0:
            self.succ = Person(self.pos+1)
            return self.succ.createChain(n-1)
        else:
            return self

    # Kills in a circle, getting every nth living person
    # When there is only one remaining, the lone survivor is returned
    def kill(self,pos,nth,remaining):
        if self.alive == 0: return self.succ.kill(pos,nth,remaining)
        if remaining == 1: return self
        if pos == nth:
            self.alive = 0
            pos=0
            remaining-=1
        return self.succ.kill(pos+1,nth,remaining)

# n people in a circle
# kill every mth person
n = 40
m = 3

first = Person(1)
last = first.createChain(n-1)
last.succ = first

print "In a circle of %d people, killing number %d" % (n,m)
winner = first.kill(1,m,n)
print "Winner: ", winner

