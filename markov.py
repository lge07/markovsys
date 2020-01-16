# Includes a Markov element and Markov Chain class

# Markov Element contains and organises the probabilities
# Markov Chain class allows modification.

# Take mTransitions.
# Create lists with the properties required.

import pickle
from numpy.random import choice
class TransitionT:
    # A data type that's basically a tally mark
    def __init__(self,to,fr):
        self.to = to
        self.fr = fr
        self.occurances = 0
        self.prob = 0
    def __eq__(self,other):
        if isinstance(other,TransitionT):
            return (self.to == other.to) and (self.fr == other.fr)
        return False
    


class mChain:
    def __init__(self,text):
        # Text should be a split version of whatever needs to be "trained"
        self.text = text
        self.allTransitions = []
        self.stateNames = {}
        self.getStates()
        self.tallyStates()
        self.oTransition()
        self.calcProb()

    def getStates(self):
        # Get all possible states
        for x in self.text:
            d = {"name":x,"total":0,"transitions":[]}
            self.stateNames[x]= d
    
    def tallyStates(self):    
        # Tally the whole text
        count = 0
        while True:
            if count==len(self.text)-1:
                break
            curr = self.text[count]
            aft = self.text[count+1]
            self.allTransitions.append(TransitionT(aft,curr))
            count+=1
        #for x in self.allTransitions:
            #print("%s -> %s" %(x.fr,x.to))

    def oTransition(self):
        for x in self.allTransitions:
            ct = self.allTransitions.count(x)
            add = x
            add.occurances = ct
            self.stateNames[x.fr]["transitions"].append(add)
            self.stateNames[x.fr]["total"]+=ct
            self.allTransitions = list(filter((x).__ne__, self.allTransitions))
        #for x in self.stateNames:
        #    for y in x["transitions"]:
        #        print("%s -> %s" %(y.fr,y.to))
        #        print(y.occurances)
        # TODO: Since this is where everything fails, use pre-generated things and 
        # search through those, probably far easier and less bad.

    def calcProb(self):
        for x in self.stateNames:
            # x will be the name
            for a in self.stateNames[x]["transitions"]:
                a.prob = a.occurances/self.stateNames[x]["total"]
    def generate(self,start,leng):
        # Based on starting element, attempt to generate chain of length
        ret = [start]
        while len(ret)<leng:
            p = ret[len(ret)-1]
            nexterm = self.stateNames[p]["transitions"]
            probs = [x.prob for x in nexterm]
            c = choice(nexterm,1,p = probs).tolist()[0]
            ret.append(c.to)
        return ret

    def preserve(self):
        pickle.dump(self.stateNames,open("markov.p","wb"))
        # list.count is useable in this case :D store all possible states as a first thing and then iterate through, adding as needed.

x = mChain(["a","b","c","b","b","a","b","c"])
print(x.generate("a",5))