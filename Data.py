class Data:
    
    
    def __init__(self):
        self.profileDictionary = {}
        self.profileSets = {}
        self.uniqueProfiles = set()        
    
    def setProfileDictionary(self, profileDict):
        self.profileDictionary = profileDict
        
    def setUniqueProfiles(self, uniqueProfiles):
        self.uniqueProfiles = uniqueProfiles
        
    def setProfileSets(self, profileSets):
        self.profileSets = profileSets
        
    def getProfileDictionary(self):
        return self.profileDictionary
    def getProfileSets(self):
        return self.profileSets
    def getUniqueProfiles(self):
        return self.uniqueProfiles
        
    
        
        