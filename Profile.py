class Profile:
    
    def __init__(self,word):
        self.profileName = word
        self.associatedWords = {}
        self.observers = []
    
    def addObservers(self,ob):
        self.observers.append(ob)
    def removeObservers(self,ob):
        self.observers.remove(ob)
    def updateObservers(self):
        for ob in self.observers:
            ob.update(self.profileName)
            
    def addNewProfile(self, addWord):
        if(str(addWord) not in self.associatedWords):
            self.associatedWords[str(addWord)] = 1
        else:
            self.associatedWords[str(addWord)] += 1
        self.updateObservers()
            
    def getProfileName(self):
        return self.profileName
     
    def getListOfWords(self):
        return self.associatedWords
    
    def addAssociatedWords(self, sentence, commonWords):
        for word in sentence.split(' '):
            if word != self.profileName and word != '' and word not in commonWords:
                self.addNewProfile(word)
            
    def __repr__(self):
        string = "\nWord: " + self.profileName + "\n\n" + "Profile:" + "\n"
        for key in self.associatedWords:
            string += "Associated Word: " + key + " Occurence: " + str(self.associatedWords[key]) + "\n"
        return string

   

