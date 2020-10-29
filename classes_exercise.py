class Student:

    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_="student"
    
    def test_score(self, score_1, score_2, score_3):
        total = score_1 + score_2 +score_3
        avg = total / 3
        return avg

callum = Student("callum", 25, "maths")






