from UndetectDriver import Driver
from selenium.webdriver.common.action_chains import ActionChains
from course import Course
import pathing
from secrets import FILE, PORT, URL
from bot import RegBot

class Algorithm:
    def __init__(self, file= FILE, port= PORT, sem= 2):
        self.file= open(file, 'r')
        self.bot = RegBot(port, sem)

    def read_file(self):
        for line in self.file:
            self.bot.add_course(line)
        
    def plan(self):
        try:
            active = False
            for course in self.bot.courses:
                if not course.isRegistered:
                    self.bot.add_course_to_Planner(course)
                    active = True
            
            return active
        except:
            print("Registered Failed!")
            return False

    def register(self):
        try:
            active = False
            for course in self.bot.courses:
                if not course.isRegistered:
                    self.bot.add_course_to_Sched(course)
                    active = True
            
            return active
        except:
            print("Registered Failed!")
            return False
    
if __name__ == '__main__':
    alg = Algorithm(file = FILE)
    alg.read_file()
    
    while alg.register():
        pass

