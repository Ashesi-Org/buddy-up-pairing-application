def pairingConstant(gender, listofcs, listoffs):
    
    if gender=="Male" or gender=="Female":
        sumcon =1

        for c in listofcs:
            if(c.getGender()==gender):
                sumcon+=c.getCardinality()

        sumfres =1

        # count male/females in incoming class.     
        for f in listoffs:
            if(f.getGender()==gender):
                sumfres+=1

        try:
            result = sumcon/sumfres
            if(result > 1):
                return True
            else:
                return False 
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")
    else:
        return "wrong parameter passed [in pairingConstant module]" 