#do a progress bar on the display screen

#importing student profiles/objects
from createobjects import continuingStudentObjects
from createobjects import freshmenObjects

listofcontinuingstudents = continuingStudentObjects()
listoffreshmen = freshmenObjects()

print(len(listofcontinuingstudents), len(listoffreshmen))

'''
    @brief: pairing constant determines if the number of continuing student present and their 
    cardinality guarantees the pairing of all male and female freshmen. 

    @return: true if value is greater than 1 else false. If it is 'True' then they are as many or more 
    continuing females/males for the fresher females/males and vice versa
'''

def pairingConstant(gender):

    if gender=="Male" or gender=="Female":
        sumcon =0

        for c in listofcontinuingstudents:
            if(c.getGender()==gender):
                sumcon+=c.getCardinality()

        sumfres =0

        # count male/females in incoming class.     
        for f in listoffreshmen:
            if(f.getGender()==gender[0]):
                sumfres+=1

        if(sumcon/sumfres > 1):
            return True
        else:
            return False 
    else:
        return "wrong parameter passed [in pairingConstant module]" 
        

    
# Ensure that Ghana is the last option in the list of preferred nationalities 
def moveGhana(continuingstudent):
    list = continuingstudent.getPreferredNationality()
    if len(list)>1 and "Ghana" in list:
        list.remove("Ghana")
        list.insert(len(list), "Ghana") #insert at the end of the list
    continuingstudent.setPreferredNationality(list)
    return continuingstudent

# Function to return the pairing description when pairing has been done.
def pairDescription(number, continuingstudent, pairsummary, pair):
    pairsummary["continuingstudent"] = continuingstudent
    pairsummary["freshers"] = pair

    if continuingstudent.getCardinality()==len(pair): # complete pairing
        listofcontinuingstudents.remove(continuingstudent)
        pairsummary["status"] = "complete"
    else: #incomplete pairing
        pairsummary["status"] = "incomplete"
    return pairsummary
    

def pairing(continuingstudent, freshmen, exceptcountry):
    pair = []
    pairsummary ={}

    # Base pairing: continuing students wants x number of freshers from the same nationality, without exceptions ("None") AND
    # secondary pairing: continuing student wants x number of freshers from N different nationalities without exceptions

    if exceptcountry[0]=="None":
        # Ensure that Ghana is the last option in the list of preferrednationalities if it was specified.
        continuingstudent= moveGhana(continuingstudent)

        for i in range(continuingstudent.getCardinality()):
        
            if len(continuingstudent.getPreferredNationality())==1:
                for f in freshmen:
                    # pairing when "Any" is in nationality
                    if "Any" in continuingstudent.getPreferredNationality()[0]:
                        if continuingstudent.getGender()[0]== f.getGender()[0]:
                            pair.append(f)
                            listoffreshmen.remove(f) # remove paired fresher 
                            break 

                    # pairing when countries specified                    
                    elif f.getNationality() in continuingstudent.getPreferredNationality() and continuingstudent.getGender()[0]== f.getGender():
                        pair.append(f)
                        listoffreshmen.remove(f) # remove paired fresher 
                        break
                    else:
                        continue
            elif len(continuingstudent.getPreferredNationality())>1:
                for f in freshmen: 
                    if f.getNationality() in continuingstudent.getPreferredNationality() and continuingstudent.getGender()[0]== f.getGender():
                        pair.append(f)
                        listoffreshmen.remove(f)
                        break
                    else:
                        continue
            
            if i==continuingstudent.getCardinality()-1: # condition checks if pairing is complete
                pairsummary = pairDescription(i, continuingstudent, pairsummary, pair)
                return pairsummary
            else: 
                continue           

    #  it has country(ies) not 'None'
    elif exceptcountry[0]!="None": 
        index = 0
        for i in range(continuingstudent.getCardinality()):
            country = exceptcountry[index]
            for f in freshmen:
                # don't pair with a fresher of the 'except nationality' 
                if country!=f.getNationality() and continuingstudent.getGender()[0]== f.getGender():
                    pair.append(f) 
                    listoffreshmen.remove(f) # remove paired fresher
                    break
                else:
                    continue

            if i==continuingstudent.getCardinality()-1: # condition checks if pairing is complete
                pairsummary = pairDescription(i, continuingstudent, pairsummary, pair)
                return pairsummary
            else: 
                # if continuing student specified more than one 'except country' so we can increase the index.
                if len(exceptcountry)-index>1: 
                    index+=1
                    continue
                else:
                    #keep the index unchanged
                    continue              
    else:  
        return 404 #error message


class Edges:    
    def __init__(self, listofcontinuingstudents, listoffreshmen):
        self.listofcontinuingstudents = listofcontinuingstudents
        self.listoffreshmen = listoffreshmen
        self.paired=dict()
        self.matched = []

    def getMatched(self):
        return self.matched
    
    def matching(self):
        reservedpairs = []

        # first check if they're enough male and female continuing students to be paired with male freshers
        if pairingConstant("Male")==True:
            if pairingConstant("Female")==True:
                for c in listofcontinuingstudents:
                    exceptcountry = []            
                    pnationality = c.getPreferredNationality()
                    for country in pnationality:
                        # first check if 'not country' exist
                        if "Not" in country:
                            exceptcountry.append(country.split("Not")[1])
                            break
                        elif "Any" in country: 
                            exceptcountry.append("None")
                            break
                        else: 
                            exceptcountry.append("None") # a case where we have actual countries.

                    # Commence pairing
                    if(len(listoffreshmen)==0):
                        print("Hurray, match is complete")
                        return self.matched,reservedpairs
                    else:
                        summary = pairing(c, listoffreshmen, exceptcountry)     
                    
                    print('\n',summary['continuingstudent'].toString())
                    for i in range(len(summary['freshers'])):
                        print(summary['freshers'][i].toString())

                    #**
                    # this part of the code is getting too big, create another function for this
                    # next this is the part that would be useful for writing paired information to dataframe.
                    #**

                    # a pairing summary status may or may not be complete, 
                    # if status is complete, append the paired item into the list.
                    if summary["status"]=="complete":
                        self.paired["continuingstudent"] = summary["continuingstudent"]
                        self.paired["freshers"] = summary["freshers"]
                        self.matched.append(self.paired)
                        print('I am complete')
                    elif summary["status"] == "incomplete":
                        self.paired["continuingstudent"] = summary["continuingstudent"]
                        self.paired["freshers"] = summary["freshers"]
                        if(len(summary["freshers"])==0):
                            print('I am incomplete: I don\'t have any of my freshers')
                            reservedpairs.append(self.paired)
                        else:
                            print('I am incomplete: I don\'t have all of my freshers')
                        
                    else: 
                        continue
            else:
                print("Error: Not enough females for pairing, repopulate female cardinality and then do matching again.")   
        else: 
            print("Error: Not enough males for pairing, repopulate male cardinality and then do matching again.")      
    
    # with reserved pairs, check if they're freshers that have not been paired and add them.
    
edges = Edges(listofcontinuingstudents, listoffreshmen)

matched, reserved = edges.matching()

print(len(listofcontinuingstudents), len(listoffreshmen))