"""
    Definition for a course
"""

class Course:
    def __init__(self, couse_txt):
        """
            course_txt: text representation of a course
            with attibutes college, department, number, and section
            seperated by whitespace
        """
        attributes = couse_txt.split(" ")
        # print("attributes= ", attributes)
        self.college = attributes[0]
        self.dept = attributes[1]
        self.number = attributes[2]
        self.section = attributes[3]
        self.isRegistered = False
    
    def __repr__(self):
        s = self.college + " " + self.dept + self.number + " " + self.section
        return s
    def __str__(self):
        s = self.college + " " + self.dept + self.number + " " + self.section
        return s

if __name__ == '__main__':
    course = Course("CAS CS 411 A1")
    print(course)