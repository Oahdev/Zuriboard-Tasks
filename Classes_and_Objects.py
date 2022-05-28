# Classes and Objects

class Student:
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def change_name(self,name):
        self.name = name
    def change_age(self,age):
        self.age = int(age)
    def add_track(self,tracks):
        self.tracks = tracks
    def get_score(self):
        print(self.name+"'s score: "+str(self.score))

def profile(id):
    details = "Name: "+id.name+"\nAge: "+str(id.age)+"\nTracks: "+id.tracks+"\nScore: "+str(id.score)
    print(details)
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Dayo = Student("Dayo",22,"BE",25.20)
Olamide = Student("Olamide",19,"Full-Stack",19.80)

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
profile(Olamide)