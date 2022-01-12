from UndetectDriver import Driver
from secrets import URL, SpringReg_url
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

def to_registration(driver, actions):    
    try:
        academic_tab= driver.find_element(By.LINK_TEXT, "University Class Schedule, Classes, ...")
        actions.click(academic_tab).perform()

        registration = driver.find_element(By.LINK_TEXT, "Registration")
        actions.click(registration).perform()   
        return   
    except:
        print("Can't find classes")

    try:
        time.sleep(3)
        button = driver.find_element(By.CLASS_NAME, "input-submit")
        actions.click(button).perform()
        return 
    except:
        print("cant find button")


def to_reg_opt(driver, actions, sem=2):
    """
        go to the reg options for the specified semester
        1: current semester
        2: next semester
    """
    to_registration(driver, actions)
    try:
        time.sleep(0.5)
        reg_option= driver.find_element(By.XPATH, f"(//a[text()= 'Reg Options'])[{sem}]")
        actions.click(reg_option).perform()
        return
    except:
        print("Can't find regopt")

def to_plan(driver, actions, sem = 2):
    to_reg_opt(driver, actions, sem)

    try:
        time.sleep(0.5)
        plan = driver.find_element(By.PARTIAL_LINK_TEXT, "Plan")
        actions.click(plan).perform()
        return
    except:
        pass

def to_register_for_class(driver, actions, sem=2):
    to_reg_opt(driver, actions, sem)
    try:
        time.sleep(0.5)
        register = driver.find_element(By.PARTIAL_LINK_TEXT, "Register for Class")
        actions.click(register).perform()
        return 
    except:
        pass

def open_tab(driver):
    #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    driver.execute_script("window.open('');")
    #ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()

def close_tab(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w').perform
    #ActionChains(driver).key_down(Keys.CONTROL).send_keys('w').key_up(Keys.CONTROL).perform()

if __name__ == '__main__':
    driver = Driver(1710).create()
    driver.get(URL)
    actions = ActionChains(driver)
    to_plan(driver, actions)
    open_tab(driver)
    driver.switch_to.window(driver.window_handles[1])
    #close_tab(driver)
    driver.get(URL)

