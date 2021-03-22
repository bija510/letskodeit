import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


class Test_multipleWindow():
##############################################################################################
    def test1(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

        driver.find_element_by_xpath("//a[@id='opentab']").click()
        time.sleep(2)
        print(driver.window_handles.count)

        windHandl = driver.window_handles
        for item in windHandl:
            print(item)

        driver.switch_to.window(driver.window_handles[1])
        print(driver.find_element_by_xpath("//span[contains(text(),'World class')]").text)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
##############################################################################################
    def test2(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successful")
##############################################################################################

cc= Test_multipleWindow()
cc.test()