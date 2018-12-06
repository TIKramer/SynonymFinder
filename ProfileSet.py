import math
#insertion 
class ProfileSet:
    class ScoredProfile:
        def __init__(self,profile, score):
            self.profile = profile
            self.score = score
        
        def getProfile(self):
            return self.profile
        def getProfileName(self):
            return self.profile.getProfileName()
        def getScore(self):
            return self.score
        
        def __repr__(self):
            string = "Profile Name: " + str(self.profile.getProfileName()) + " Score:" + str(self.getScore())
        
            return string

        
    def sort(self):
        self.insertionSort()
        
    def __init__(self,mainProfile, unScoredProfiles):
        self.profile = mainProfile
        self.scoredProfiles = []
        self.scoreProfiles(unScoredProfiles)
        mainProfile.addObservers(self)


    def addNewProfile(self, addNewProfile):
        if(addNewProfile not in scoredProfiles):
            self.scoredProfiles[addNewProfile] = compareTwoProfiles(self.profile, addNewProfile)

    def __repr__(self):
        string = "ProfileList:\n " + str(self.profile.getProfileName()) + "\n"
        for profile in self.scoredProfiles:
            string += "Profile: " + str(profile) + "\n"
        
        return string


    def scoreProfiles(self,unScoredProfiles):
        for profile in unScoredProfiles:
            score = self.compareTwoProfiles(self.profile, profile)
            scoredProfile = self.ScoredProfile(profile,score)
            self.scoredProfiles.append(scoredProfile)
            self.sort()
    
    def rescoreProfiles(self):
         for profile in self.scoredProfiles:
            profile.score = self.compareTwoProfiles(self.profile, profile.getProfile())
            self.sort()
            
    def compareTwoProfiles(self,profile1, profile2):
        listWordsProfile1 = profile1.getListOfWords()
        listWordsProfile2 = profile2.getListOfWords()
        value = 0
        pVector, qVector = 0, 0
        for word in listWordsProfile2:
            qVector += listWordsProfile2[word] * listWordsProfile2[word]
        for word in listWordsProfile1:
            if word in listWordsProfile2:
                value = value + listWordsProfile1[word] * listWordsProfile2[word]
            pVector += listWordsProfile1[word] * listWordsProfile1[word]
        if pVector != 0 and qVector != 0:
            endValue = value/math.sqrt(pVector*qVector)
        else:
            endValue = 0
        return endValue
    
    def update(self,profileName):
        runUpdate = False;
        if(profileName == self.profile.getProfileName()):
            runUpdate = True
        for profile in self.scoredProfiles:
            if profile.getProfileName() == profileName:
                runUpdate = True;
        if(runUpdate):
            self.rescoreProfiles()
    
    def insertionSort(self):
      # print("Starting sort")
        
       for index in range(1,len(self.scoredProfiles)):
         currentvalue = self.scoredProfiles[index]
         position = index
        # print("index" + str(index))
         while position > 0 and self.scoredProfiles[position-1].getScore() < currentvalue.getScore():
            # print("looped" + str(position))
             self.scoredProfiles[position]=self.scoredProfiles[position-1]
             position = position-1
           #  print("update" + str(position))

         self.scoredProfiles[position]=currentvalue
         
	
