
import unittest
import HTMLTestRunner
from selenium import webdriver
from unittest_data_provider import data_provider



class TestTestingBotClient(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
        self.driver.implicitly_wait(15)
    
    def tearDown(self):
        self.driver.quit()

    text = lambda: (
        (("lala"),"hello"),                 
        (("haha"),"byee")                
    )
    
    colors = lambda: (
        ( ( ), 'hello' ),
        ( ( ), 'bye' ),
        ( ( ), 'hi' ),
        ( ( ), 'black' )
    )
    
    @data_provider(text)
    def test_google_example(self, color, notatio):
        self.driver.get("http://www.google.com")
        if not "Google" in self.driver.title:
            raise Exception("Unable to load google page!")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys(notatio)
        elem.send_keys(color)
        elem.submit()
        
    @data_provider(colors)
    def test_ynet_example(self, color, notation):
        self.driver.get("http://www.walla.co.il")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys(notation)
        elem.submit()


    

if __name__ == '__main__':
    #unittest.main()
    HTMLTestRunner.main()