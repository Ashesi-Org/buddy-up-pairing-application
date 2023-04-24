class Continuing:
    def __init__(self, name, gender, preferred_nationality, nationality,cardinality):
        self.name = name
        self.p_nationality = preferred_nationality
        self.gender = gender
        self.nationality = nationality
        self.cardinality = int(cardinality)

    # GETTERS

    def getName(self):
        return self.name
    
    def getPreferredNationality(self):
        return self.p_nationality
    
    def getGender(self):
        return self.gender
    
    def getCardinality(self):
        return self.cardinality
    
    def getNationality(self):
        return self.nationality

    # SETTERS

    def setName(self, name):
        self.name=name
    
    def setPreferredNationality(self,nationality):
        self.p_nationality=nationality

    def setGender(self,gender):
        self.gender=gender
    
    def setCardinality(self,cardinality):
        self.cardinality=int(cardinality)
    
    def setNationality(self,nationality):
        self.nationality= nationality

    # TOSTRING

    def toString(self):
        return "name: "+self.name,"preferred nationality: " +\
            str(self.p_nationality),"gender: "+\
                self.gender,"nationality: "+self.nationality,\
                "cardinality: "+str(self.cardinality)
