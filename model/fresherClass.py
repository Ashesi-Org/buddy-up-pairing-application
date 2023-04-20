
class Fresher:
    def __init__(self, name, gender, nationality):
        self.name = name
        self.gender = gender
        self.nationality = nationality
    
    # GETTERS

    def getName(self):
        return self.name
    
    def getNationality(self):
        return self.nationality
    
    def getGender(self):
        return self.gender

    # SETTERS 

    def setName(self, name):
        self.name = name
    
    def setNationality(self,nationality):
        self.nationality=nationality
    
    def setGender(self,gender):
        self.gender=gender
    
    #TOSTRING

    def toString(self):
        return "name: "+self.name, "nationality: "+\
            self.nationality,"gender: "+self.gender
