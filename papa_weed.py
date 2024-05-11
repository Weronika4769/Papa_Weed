# LOGGING IN TESTS FOR 'PAPA WEED' WEBSITE

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


# LOGGING TEST DATA

correct_email = "testing.papaweed@gmail.com"
fake_email = "fake.email@fake.com"
correct_password = "TestingUser123!"
fake_password = "fake.password"
expected_user_name = "testing.papaweed"


# TEST CASE ID_1

class loggingInTest1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://papaweed.pl/")
        sleep(5)
        cookie = self.driver.find_element(By.CSS_SELECTOR, "#cn-accept-cookie")
        cookie.click()
        sleep(5)
        action = ActionChains(self.driver)
        shop = self.driver.find_element(By.CSS_SELECTOR, "#menu-item-403 > a")
        action.move_to_element(shop).perform()
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/ul/li[2]/a"))
        )
        my_account.click()
        sleep(5)

    def testCase_ID_1(self):
        email = self.driver.find_element(By.ID, "username")
        email.send_keys(correct_email)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(correct_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)
        # EXPECTED RESULT
        actual_user_name = self.driver.find_element(By.CSS_SELECTOR, "#post-101 > div > div.woocommerce > div > p:nth-child(2) > strong:nth-child(1)")
        self.assertEqual(actual_user_name.text, expected_user_name)
        if actual_user_name.text == expected_user_name:
            print("ID_1: User login succeeded!")
        sleep(5)

    def tearDown(self):
            self.driver.quit()


# TEST CASE ID_2

class loggingInTest2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://papaweed.pl/")
        sleep(5)
        cookie = self.driver.find_element(By.CSS_SELECTOR, "#cn-accept-cookie")
        cookie.click()
        sleep(5)
        action = ActionChains(self.driver)
        shop = self.driver.find_element(By.CSS_SELECTOR, "#menu-item-403 > a")
        action.move_to_element(shop).perform()
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/ul/li[2]/a"))
        )
        my_account.click()
        sleep(5)

    def testCase_ID_2(self):
        email = self.driver.find_element(By.ID, "username")
        email.send_keys(fake_email)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(fake_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)
        # EXPECTED RESULT
        timeout = 5
        failed_log_in_announcement = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )
        if failed_log_in_announcement.is_displayed():
            print("ID_2: Error announcement. Unknown e-mail address. Login failure.")
        sleep(5)

    def tearDown(self):
        self.driver.quit()


# TEST CASE ID_3

class loggingInTest3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://papaweed.pl/")
        sleep(5)
        cookie = self.driver.find_element(By.CSS_SELECTOR, "#cn-accept-cookie")
        cookie.click()
        sleep(5)
        action = ActionChains(self.driver)
        shop = self.driver.find_element(By.CSS_SELECTOR, "#menu-item-403 > a")
        action.move_to_element(shop).perform()
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/ul/li[2]/a"))
        )
        my_account.click()
        sleep(5)

    def testCase_ID_3(self):
        email = self.driver.find_element(By.ID, "username")
        email.send_keys(fake_email)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(correct_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)
        # EXPECTED RESULT
        timeout = 5
        failed_log_in_announcement = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )
        if failed_log_in_announcement.is_displayed():
            print("ID_3: Error announcement. Unknown e-mail address. Login failure.")
        sleep(5)

    def tearDown(self):
        self.driver.quit()


# TEST CASE ID_4

class loggingInTest4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://papaweed.pl/")
        sleep(5)
        cookie = self.driver.find_element(By.CSS_SELECTOR, "#cn-accept-cookie")
        cookie.click()
        sleep(5)
        action = ActionChains(self.driver)
        shop = self.driver.find_element(By.CSS_SELECTOR, "#menu-item-403 > a")
        action.move_to_element(shop).perform()
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/ul/li[2]/a"))
        )
        my_account.click()
        sleep(5)

    def testCase_ID_4(self):
        email = self.driver.find_element(By.ID, "username")
        email.send_keys(correct_email)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(fake_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)
        # EXPECTED RESULT
        timeout = 5
        failed_log_in_announcement = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )
        if failed_log_in_announcement.is_displayed():
            print("ID_4: Error announcement. Unknown e-mail address. Login failure.")
        sleep(5)

    def tearDown(self):
        self.driver.quit()


# TEST CASE ID_5

class loggingInTest5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://papaweed.pl/")
        sleep(5)
        cookie = self.driver.find_element(By.CSS_SELECTOR, "#cn-accept-cookie")
        cookie.click()
        sleep(5)
        action = ActionChains(self.driver)
        shop = self.driver.find_element(By.CSS_SELECTOR, "#menu-item-403 > a")
        action.move_to_element(shop).perform()
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/ul/li[2]/a"))
        )
        my_account.click()
        sleep(5)

    def testCase_ID_5(self):
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(correct_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)
        # EXPECTED RESULT
        timeout = 5
        failed_log_in_announcement = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )
        if failed_log_in_announcement.is_displayed():
            print("ID_5: Error announcement. E-mail address is required. Login failure.")
        sleep(5)

    def tearDown(self):
        self.driver.quit()


# TEST CASE ID_6

class loggingInTest6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://papaweed.pl/")
        sleep(5)
        cookie = self.driver.find_element(By.CSS_SELECTOR, "#cn-accept-cookie")
        cookie.click()
        sleep(5)
        action = ActionChains(self.driver)
        shop = self.driver.find_element(By.CSS_SELECTOR, "#menu-item-403 > a")
        action.move_to_element(shop).perform()
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/ul/li[2]/a"))
        )
        my_account.click()
        sleep(5)

    def testCase_ID_6(self):
        page_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, arguments[0] / 2);", page_height)
        email = self.driver.find_element(By.ID, "username")
        email.send_keys(correct_email)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)
        # EXPECTED RESULT
        timeout = 5
        failed_log_in_announcement = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )
        if failed_log_in_announcement.is_displayed():
            print("ID_6: Error announcement. Password field is empty. Login failure.")
        sleep(5)

    def tearDown(self):
        self.driver.quit()


# TEST CASE ID_7

class loggingInTest7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://papaweed.pl/")
        sleep(5)
        cookie = self.driver.find_element(By.CSS_SELECTOR, "#cn-accept-cookie")
        cookie.click()
        sleep(5)
        action = ActionChains(self.driver)
        shop = self.driver.find_element(By.CSS_SELECTOR, "#menu-item-403 > a")
        action.move_to_element(shop).perform()
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/ul/li[2]/a"))
        )
        my_account.click()
        sleep(5)

    def testCase_ID_7(self):
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(10)
        # EXPECTED RESULT
        timeout = 5
        failed_log_in_announcement = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )
        if failed_log_in_announcement.is_displayed():
            print("ID_7: Error announcement. Email address is required. Login failure.")
        sleep(5)

    def tearDown(self):
        self.driver.quit()