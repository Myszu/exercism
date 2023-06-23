class Garden:
    def __init__(self, diagram: str, students: list = []):
        if not students:
            # Just as I find it cleaner, then pushing into default value.
            students = [
                'Alice', 'Bob', 'Charlie', 'David',
                'Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry'
            ]
        self.students = students.copy()
        self.students.sort()
        self.diagram = diagram
        self.saplings = {
            'G':'Grass',
            'C':'Clover',
            'R':'Radishes',
            'V':'Violets'
        }
        
        
    def plants(self, student):
        self.student = student
        rows = self.diagram.split()
        beds = {}
        for i, kid in enumerate(self.students):
            if kid == self.student:
                for row in rows:
                    try:
                        beds[kid] += self.identify(row[i*2:i*2+2])
                    except KeyError:
                        beds[kid] = self.identify(row[i*2:i*2+2])
        return beds[self.student]
                    
    
    def identify(self, bed):
        output = []
        for plant in bed:
            output.append(self.saplings.get(plant))
        return output
