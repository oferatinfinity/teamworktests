import time
import unittest
from selenium import webdriver
import page

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(40)
        self.driver.get("https://topq.teamwork.com")

    def tearDown(self):
        self.driver.quit()


    def testName(self):
        tasklistname = "yabadaba";
        pge = page.LoginPage(self.driver)
        pge = pge.loginr("fake11@fake.com", "fake")
        pme = pge.clickTasks()
        time.sleep(5)
        pre = pme.addTaskList()
        pse = pre.addTaskList(tasklistname)
        pfv = pse.clickTaskList(tasklistname)
        pfv.clickAdd()
        pfv.addTask("task1")
        time.sleep(5)
        pfv.addTask("task2")
        milepage = pfv.clickMilestones()
        pre = milepage.clickTasks()
        tpage = pre.clickTaskList(tasklistname)
        self.assertEqual(tpage.cntList(),1)
        tpage.delTaskList()
        time.sleep(5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()