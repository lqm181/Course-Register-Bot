"""
    bot.py: define a bot that can register for classes
"""
from selenium.webdriver.common.by import By
from UndetectDriver import Driver
from secrets import PORT, URL
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pathing
from course import Course
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

class RegBot:
    def __init__(self, port= PORT, sem= 2):
        self.driver = Driver(port).create()
        self.actions = ActionChains(self.driver)
        
        self.courses = []
        self.sem = sem

    def add_course(self, course_name):
        self.courses.append(Course(course_name))
    
    def add_courses(self, course_list):
        for course in course_list:
            self.add_course(course)

    def search_class(self, course):
        #Select college
        select = Select(self.driver.find_element(By.NAME, "College"))
        select.select_by_visible_text(course.college)
        
        # Input Department name
        dept_fill = self.driver.find_element(By.NAME, "Dept")
        dept_fill.clear()
        dept_fill.send_keys(course.dept)

        # Input for Course number 
        number_fill = self.driver.find_element(By.NAME, "Course")
        number_fill.clear()
        number_fill.send_keys(course.number)

        # Click the go button
        go_button= self.driver.find_element(By.XPATH, "//input[@type= 'button'][@onclick='SearchSchedule()']")
        self.actions.click(go_button).perform()

    def add_course_to_Planner(self, course):
        windows= self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.get(URL)
        pathing.to_plan(self.driver, self.actions)

        # Navigate to Add option
        add_button = self.driver.find_element(By.LINK_TEXT, "Add")
        self.actions.click(add_button).perform()

        # Search class options
        # We will get a list of available classes
        self.search_class(course)

        # Choose classes that are lectures
        checkboxes = self.driver.find_elements(By.XPATH, "//tr[td[8]/text()= 'Lecture']/td[1]/input[@type='checkbox']")
        class_names = self.driver.find_elements(By.XPATH, "//tr[td[8]/text()= 'Lecture'][td[1]/input/@type='checkbox']/td[3]")
        
        if len(checkboxes) > 0: 
            # Make a list of classname: checkbox
            d = {class_names[i].text: checkboxes[i] for i in range(len(checkboxes))}
            
            if str(course) in d:
                # clickcheckbox on this course
                self.actions.click(d[str(course)]).perform()
            else:
                # click the checkbox of the an another course
                self.actions.click(checkboxes[0])

            # click add to planner
            add_planner_button = self.driver.find_element(By.XPATH, "//input[@type= 'button'][@value= 'Add to Planner']")
            self.actions.click(add_planner_button).perform()
            
            course.isRegistered = True
        else:
            # Can't find any classes -> do nothing
            pass
        
        # Add an empty page to keep the localhost running
        pathing.open_tab(self.driver)
        # Close the driver
        self.driver.close()

    def add_course_to_Sched(self, course):
        windows= self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.get(URL)
        pathing.to_register_for_class(self.driver, self.actions)
        

        # Search class options
        # We will get a list of available classes
        self.search_class(course)
        
        # Choose classes that are lectures
        checkboxes = self.driver.find_elements(By.XPATH, "//tr[td[8]/text()= 'Lecture']/td[1]/input[@type='checkbox']")
        class_names = self.driver.find_elements(By.XPATH, "//tr[td[8]/text()= 'Lecture'][td[1]/input/@type='checkbox']/td[3]")
        
        if len(checkboxes) > 0: 
            # Make a list of classname: checkbox
            d = {class_names[i].text: checkboxes[i] for i in range(len(checkboxes))}
            
            if str(course) in d:
                # clickcheckbox on this course
                self.actions.click(d[str(course)]).perform()
            else:
                # click the checkbox of the an another course
                self.actions.click(checkboxes[0])

            # click add to planner
            add_button = self.driver.find_element(By.XPATH, "//input[@type= 'button'][@value= 'Add Classes to Schedule']")
            self.actions.click(add_button).perform()
            
            time.sleep(2)
            Alert(self.driver).accept()
            course.isRegistered = True
        else:
            # Can't find any classes -> do nothing
            pass
        
        # Add an empty page to keep the localhost running
        pathing.open_tab(self.driver)
        # Close the driver
        self.driver.close()
        

if __name__ == '__main__':
    bot = RegBot(PORT)
    course = Course("CAS CS 411 A1")
    bot.add_course_to_Sched(course)
    
    
    


