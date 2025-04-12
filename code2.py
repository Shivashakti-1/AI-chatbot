from selenium import webdriver
from selenium.webdriver.edge.service import Service
class infow():
    def __init__(self,driver):
        self.driver=driver
        #executable_path = r"C:\Users\shiva\PycharmProjects\pythonProject\webdriver\msedgedriver.exe"
        executable_path = r"C:\Users\shiva\Downloads\edgedriver_win64\msedgedriver.exe"
        service = Service(executable_path)
        driver = webdriver.Edge(service=service)
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")

        
    assist = infow()
    assist.get_info("newtron stars")