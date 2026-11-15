class Teacher:
    def teach(self):
        print("Professor teaches students")

class Researcher:
    def research(self):
        print("Professor conducts research")

class Professor(Teacher, Researcher):
    def work(self):
        print("Professor performs both roles")

obj = Professor()
obj.teach()
obj.research()
obj.work()