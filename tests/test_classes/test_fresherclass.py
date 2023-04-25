from model.fresherClass import Fresher

class TestFresher:
    def test_constructor(self):
        f = Fresher("John Doe", "Male", "South African")
        assert f.getName() == "John Doe"
        assert f.getGender() == "Male"
        assert f.getNationality() == "South African"

    def test_setters(self):
        f= Fresher("John Doe", "Male", "Ghanaian")
        f.setName("Jane Smith")
        assert f.getName() == "Jane Smith"
        f.setGender("Female")
        assert f.getGender() == "Female"
        f.setNationality("Canadian")
        assert f.getNationality() == "Canadian"

    def test_toString(self):
        f = Fresher("John Doe", "Male", "American")
        expected = ('name: John Doe', 'nationality: American', 'gender: Male')
        assert f.toString() == expected