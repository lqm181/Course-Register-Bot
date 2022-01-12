from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from secrets import local_PATH

class Driver:
    def __init__(self, port):
        self.port = port
    
    def create(self):
        options = Options()
        options.add_experimental_option("debuggerAddress", f'localhost:{self.port}')
        driver = webdriver.Chrome(executable_path= local_PATH, options= options)

        return driver
