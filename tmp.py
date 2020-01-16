class mTransition:
    def __init__(self,t,f,occurances,total):
        self.to = t
        self.fr = f
        self.ocurrances = occurances
        self.total = total
        self.probability = self.ocurrances/self.total

class mState:
    def __init__(self,name,transitions,chainElementCount):
        self.name = name
        self.transitions = transitions
        self.elementCount = chainElementCount
        self.verify()
    
    def verify(self):
        l = len(self.transitions)
        if l != self.elementCount:
            raise ValueError
        p = 0
        selfProb = False
        repeat = False
        for x in self.transitions:
            p+=x.probability
            if x.to==x.fr==name:
                selfProb = True
        if selfProb==False:
            raise ValueError
        if not 0.9<p<1.1:
            raise ValueError
        
    # Handle the collection of transitions, make sure that the proper number is present and that probabilities/occurances are fine.

def sortGroup(self):
        # Sort and group by first term
        self.allTransitions.sort(key = lambda x: x.fr)
        count = 0
        last = self.allTransitions[0]
        tmp = []
        while True:
            ft = self.allTransitions[count]
            if ft==last:
                tmp.append(ft)
            if ft!=last:
                self.groupedTransitions.append(tmp)
                tmp = []
            last = ft
            count+=1
            if len(self.allTransitions)==count:
                break
    def getTotal(self):
        # Tally total number of transitions involving first term
        for x in self.groupedTransitions:
            self.stateTotals.append([x[0].fr,len(x)])
        # Tally and create individual probabilities
    