# USER LOGOUT TEST FOR 'PAPA WEED' WEBSITE

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


# TEST DATA

correct_email = "testing.papaweed@gmail.com"
correct_password = "TestingUser123!"
main_site_url = "https://papaweed.pl/"
logging_in_site_url = "https://papaweed.pl/moje-konto/"


# TEST CASE

class user_logout_test(unittest.TestCase):

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
        email = self.driver.find_element(By.ID, "username")
        email.send_keys(correct_email)
        password = self.driver.find_element(By.ID, "password")
        password.send_keys(correct_password)
        log_in = self.driver.find_element(By.CSS_SELECTOR,
                                          "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
        log_in.click()
        sleep(5)


    def test_user_logout(self):

        logging_out = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div[1]/nav/ul/li[6]/a')
        logging_out.click()
        sleep(5)

        # EXPECTED RESULT 1

        current_url_1 = self.driver.current_url
        if current_url_1 == main_site_url:
            print("User logout test OK: User logout successfully!")
        else:
            print("User Logout Test FAIL: User logout failed!")

        # ANOTHER CODE YOU CAN USE IN TEST

        # self.assertEqual(current_url_1, main_site_url, "User logout successfully!"):
        # print("User logout failed!")

        # EXPECTED RESULT 2

        action = ActionChains(self.driver)
        shop = self.driver.find_element(By.CSS_SELECTOR, "#menu-item-403 > a")
        action.move_to_element(shop).perform()
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/ul/li[2]/a"))
        )
        my_account.click()
        sleep(5)

        current_url_2 = self.driver.current_url
        self.assertEqual(current_url_2, logging_in_site_url, "User logout successfully!")
        print("User logout test OK: User logout successfully!")


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()