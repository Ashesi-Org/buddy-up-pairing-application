from model.continuingStudentClass import Continuing
from model.fresherClass import Fresher
from model.pairingConstant import pairingConstant

def test_pairingConstant():
    # Create some Continuing students and Freshmen to use in the test
    c1 = Continuing("John", "Male", "Ghana", "South African", 4)
    c2 = Continuing("Mary", "Female", "Cameroon", "Togolese", 2)
    c3 = Continuing("Bob", "Male", "Australia", "Australia", 3)
    f1 = Fresher("Alice", "Female", "Cameroon")
    f2 = Fresher("Sam", "Male", "Ghana")
    f3 = Fresher("Jill", "Female", "Australia")
    
    # Add the students to the appropriate lists
    listofcontinuingstudents = [c1, c2, c3]
    listoffreshmen = [f1, f2, f3]
    
    # Test the function with the Male gender
    assert pairingConstant("Male",listofcontinuingstudents,listoffreshmen) == True
    
    # Test the function with the Female gender
    assert pairingConstant("Female",listofcontinuingstudents,listoffreshmen) == False
    
    # Test the function with an invalid gender
    assert pairingConstant("InvalidGender",listofcontinuingstudents,listoffreshmen) == "wrong parameter passed [in pairingConstant module]"
