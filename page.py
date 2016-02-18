from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tkinter.font import nametofont

class Apage():
    def __init__(self,driver):
        self.driver = driver

class MainBar(Apage):
    
    def __init__(self,driver):
        self.driver = driver
        self.taskPageBtn = (By.ID,"tab_tasks")
        self.milestonesPageBtn = (By.ID,"tab_milestones")
    def clickTasks(self):
        self.driver.find_element(*self.taskPageBtn).click()
        return TasksPage(self.driver)
    def clickMilestones(self):
        self.driver.find_element(*self.milestonesPageBtn).click()
        return MilestonesPage(self.driver)

class MilestonesPage(MainBar):
    def do_Noting(self):
        print("nothing")
        
class TasksPage(MainBar):
    addtasklistbtn = (By.ID,"liBFOATL")
    def addTaskList(self):
        self.driver.find_element(*self.addtasklistbtn).click()
        return AddTaskListPage(self.driver)
    
    def clickTaskList(self,name):
        self.driver.find_element_by_link_text(name).click()
        return TaskListsPage(self.driver)
    
class LoginPage(Apage):
    login = (By.ID, "userLogin")
    password = (By.ID, "password")
    lgnbtn = (By.ID, "ordLoginSubmitBtn")

    def enterUser(self, uname):
        self.driver.find_element(*self.login).clear()
        self.driver.find_element(*self.login).send_keys(uname)    
        
    def enterPass(self, upass):
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(upass)
        
    def loginr(self, uname, upass):
        self.enterUser(uname)
        self.enterPass(upass)
        self.driver.find_element(*self.lgnbtn).click()
        return MainBar(self.driver)

class TaskListsPage(MainBar):
    taskname = (By.XPATH, "//form[@id='newTaskForm']//following::span/input[@placeholder]")
    addtaskbtn = (By.XPATH, "//button[@class= 'btn btn-success js-add-task btn-lg']")
    optionsbtn = (By.XPATH, "//button[@class='btn btn-default btn-hasIcon tipped']")
    deletebtn = (By.LINK_TEXT, "Delete")
    tlist = (By.XPATH, "//div[@class='taskListContent noSel']")
    
    def clickAdd(self):
        self.driver.find_element(*self.addtaskbtn).click()
        
    def addTask(self,name):
        mydrpdwn = Select(self.driver.find_element_by_name("taskAssignedToUserId"))
        mydrpdwn.select_by_visible_text("fake11 fake11 (me)")
        self.driver.find_element(*self.taskname).send_keys(name)
        self.driver.find_element(*self.taskname).submit()
        
    def cntList(self):
        return len(self.driver.find_elements(*self.tlist))
        
    def delTaskList(self):
        self.driver.find_element(*self.optionsbtn).click()
        self.driver.find_element(*self.deletebtn).click()
        return TasksPage(self.driver)
    
class AddTaskListPage(Apage): 
    namefield = (By.ID, "newTaskListName")
    submitbtn = (By.ID, "btnCreateTaskList")
   
    def addTaskList(self, name):
        self.driver.find_element(*self.namefield).send_keys(name)
        self.driver.find_element(*self.submitbtn).click()
        return TasksPage(self.driver)
           

