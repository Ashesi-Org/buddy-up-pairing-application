from model.continuingStudentClass import Continuing

class TestContinuing:
    def test_constructor(self):
        c = Continuing("John Doe", "Male", "Canadian", "American", "3")
        assert c.getName() == "John Doe"
        assert c.getGender() == "Male"
        assert c.getPreferredNationality() == "Canadian"
        assert c.getNationality() == "American"
        assert c.getCardinality() == 3

    def test_setters(self):
        c = Continuing("John Doe", "Male", "Canadian", "American", "3")
        c.setName("Jane Smith")
        assert c.getName() == "Jane Smith"
        c.setGender("Female")
        assert c.getGender() == "Female"
        c.setPreferredNationality("Mexican")
        assert c.getPreferredNationality() == "Mexican"
        c.setNationality("Canadian")
        assert c.getNationality() == "Canadian"
        c.setCardinality(4)
        assert c.getCardinality() == 4

    def test_toString(self):
        c = Continuing("John Doe", "Male", "Canadian", "American", "3")
        expected = ('name: John Doe', 'preferred nationality: Canadian', 'gender: Male', 'nationality: American', 'cardinality: 3')
        print(c.toString())
        assert c.toString() == expected
