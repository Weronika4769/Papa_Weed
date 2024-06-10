# USER LOGIN TESTS FOR 'PAPA WEED' WEBSITE

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


# TEST DATA

correct_email = "testing.papaweed@gmail.com"
fake_email = "fake.email@fake.com"
correct_password = "TestingUser123!"
fake_password = "fake.password"
expected_user_name = "testing.papaweed"


# TEST CASES

class user_login_tests(unittest.TestCase):

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
        

    def tearDown(self):
        self.driver.quit()



    # TEST CASE ID 1: LOGIN TO USER ACCOUNT USING CORRECT EMAIL ADDRESS AND PASSWORD

    def test_case_ID_1(self):

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
            print("Test Case ID 1: User log in succeeded!")
        else:
            print("Test Case ID 1: Error found! User login failed despite providing correct login data.")
        sleep(5)



    # TEST CASE ID 2: LOGIN TO USER ACCOUNT USING INCORRECT EMAIL ADDRESS AND PASSWORD

    def test_case_ID_2(self):

        email = self.driver.find_element(By.ID, "username")
        email.send_keys(fake_email)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(fake_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)

        # EXPECTED RESULT

        failed_log_in_announcement = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )

        if failed_log_in_announcement.is_displayed():
            print("Test Case ID 2: Error announcement is displayed! User login failed as expected.")
        else:
            print("Test Case ID 2: Something goes wrong!")
        sleep(5)



    # TEST CASE ID 3: LOGIN TO USER ACCOUNT USING INCORRECT EMAIL ADDRESS AND CORRECT PASSWORD

    def test_case_ID_3(self):

        email = self.driver.find_element(By.ID, "username")
        email.send_keys(fake_email)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(correct_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)

        # EXPECTED RESULT

        failed_log_in_announcement = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )

        if failed_log_in_announcement.is_displayed():
            print("Test Case ID 3: Error announcement is displayed! User login failed as expected.")
        else:
            print("Test Case ID 3: Something goes wrong!")
        sleep(5)



    # TEST CASE ID 4: LOGIN TO USER ACCOUNT USING CORRECT EMAIL ADDRESS AND INCORRECT PASSWORD

    def test_case_ID_4(self):

        email = self.driver.find_element(By.ID, "username")
        email.send_keys(correct_email)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(fake_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)

        # EXPECTED RESULT

        failed_log_in_announcement = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )

        if failed_log_in_announcement.is_displayed():
            print("Test Case ID 4: Error announcement is displayed! User login failed as expected.")
        else:
            print("Test Case ID 4: Something goes wrong!")
        sleep(5)



    # TEST CASE ID 5: LOGIN TO USER ACCOUNT USING ONLY CORRECT PASSWORD (WITHOUT PROVIDING EMAIL ADDRESS)

    def test_case_ID_5(self):

        password = self.driver.find_element(By.ID, "password")
        password.send_keys(correct_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)

        # EXPECTED RESULT

        failed_log_in_announcement = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )

        if failed_log_in_announcement.is_displayed():
            print("Test Case ID 5: Error announcement is displayed! User login failed as expected.")
        else:
            print("Test Case ID 5: Something goes wrong!")
        sleep(5)



    # TEST CASE ID 6: LOGIN TO USER ACCOUNT USING ONLY CORRECT EMAIL ADDRESS (WITHOUT PROVIDING PASSWORD)

    def test_case_ID_6(self):

        page_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, arguments[0] / 2);", page_height)
        email = self.driver.find_element(By.ID, "username")
        email.send_keys(correct_email)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)

        # EXPECTED RESULT

        failed_log_in_announcement = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )

        if failed_log_in_announcement.is_displayed():
            print("Test Case ID 6: Error announcement is displayed! User login failed as expected.")
        else:
            print("Test Case ID 6: Something goes wrong!")
        sleep(5)



    # TEST CASE ID 7: LOGIN TO USER ACCOUNT WITHOUT PROVIDING EMAIL ADDRESS AND PASSWORD)

    def test_case_ID_7(self):

        log_in = self.driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(10)

        # EXPECTED RESULT

        failed_log_in_announcement = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/ul"))
        )

        if failed_log_in_announcement.is_displayed():
            print("Test Case ID 7: Error announcement is displayed! User login failed as expected.")
        else:
            print("Test Case ID 7: Something goes wrong!")
        sleep(5)



if __name__ == "__main__":
    unittest.main()
