# Required package
#!pip install a-world-of-countries

import awoc
from readfromfile import continuingstudents
from readfromfile import freshmen
from continuingStudentClass import Continuing as csc
from fresherClass import Fresher as fc

def getCountry(countrycode):
    my_world = awoc.AWOC()

    # some students can come from countries out of Africa, so we don't use the 
    # get_countries_list_of('continentname')
    nations = my_world.get_countries() 

    nations2 = {}

    # getting the country code for each country name
    for country in nations:
        code=country["ISO2"]
        name=country["Country Name"]
        nations2[code]=name

    countryname =nations2[countrycode]

    return countryname


def continuingStudentObjects():
    df = continuingstudents
    listofcontinuingstudents = []

    for i in range(len(df)):

        #read student attributes from dataframe
        name=df.iloc[i,0]
        gender=df.iloc[i,1]
        pnationality=df.iloc[i,3].replace(" ", "").split(',')
        cardinality=int(df.iloc[i,4])

        #create continuingstudent object
        continuingstudent = csc(name,gender,pnationality,cardinality)
        
        #append continuing student to list
        listofcontinuingstudents.append(continuingstudent)

    return listofcontinuingstudents

def freshmenObjects():
    df = freshmen

    listoffreshmen = []
    
    for i in range(len(df)):
        name = df.iloc[i,0]
        gender = df.iloc[i,1]
        nationality = df.iloc[i,2]

        #output after split: "code", "countryname"
        nation = nationality.split(' ') 
        nationality = getCountry(nation[0]).replace(" ", "")

        #create freshment object
        freshman = fc(name,gender,nationality)

        listoffreshmen.append(freshman)

    return listoffreshmen

continuingStudentObjects()