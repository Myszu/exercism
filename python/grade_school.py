class School:
    def __init__(self):
        self.output, self.history = [], []


    def add_student(self, name, grade):
        if name in self.roster():
            self.history.append(False)
        else:
            self.output.append((name, grade))
            self.history.append(True)
            self.output.sort(key=lambda sorted: (sorted[1], sorted[0]))


    def roster(self):
        return [name for name, grade in self.output]


    def grade(self, grade_number):
        return [name for name, grade in self.output if grade == grade_number]
            

    def added(self):
        return self.history
