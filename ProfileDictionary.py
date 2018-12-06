from Profile import Profile

class ProfileDictionary:
    
    def __init__(self,commonWordList):
        self.profileDict = profileDict = {}
        self.commonWordList = commonWordList
    
    def __repr__(self):
        string = "Profile Dict"
        for key in self.profileDict:
            string += self.profileDict[key].getProfileName()
        
        return string
    
    def getProfiles(self):
        return self.profileDict
    
    def addProfilesUsingSentences(self, sentences, profileLists):
            for currentSentence in sentences:
                self.addProfileUsingSentence(currentSentence, profileLists)
                
    def addProfileUsingSentence(self,currentSentence,profileList):
        wordsFoundInCurrentSentence = []
        for currentWord in currentSentence.split(' '):
                    if currentWord not in wordsFoundInCurrentSentence:
                            for aProfile in profileList:
                                if(aProfile == currentWord):
                                    wordsFoundInCurrentSentence.append(currentWord)
                                    if(aProfile not in self.profileDict):
                                        self.createNewProfile(currentWord, currentSentence)
                                    else:
                                        self.addToExsitingProfile(currentWord, currentSentence)
                                        
    def createNewProfile(self,currentWord, currentSentence):
        newProfileWord = Profile(currentWord)
        newProfileWord.addAssociatedWords(currentSentence, self.commonWordList)
        self.profileDict[currentWord] = newProfileWord
        #print("/n New Profile: " + str(self.profileDict[currentWord]) + "---\n")
        
        
    def addToExsitingProfile(self, currentWord, currentSentence):
        self.profileDict[currentWord].addAssociatedWords(currentSentence, self.commonWordList)
        
    def updateCommonWordList(self,commonWordFile):
        self.commonWordList = commonWordFile
       # print("added to profile: " + str(self.profileDict[currentWord]))
       
        
