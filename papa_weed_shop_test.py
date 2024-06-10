#  TESTING BASIC FUNCTIONALITIES IN 'PAPA WEED' ONLINE SHOP

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


# TEST DATA

shop_site_url = "https://papaweed.pl/shop/"
most_popular_tea_name = "Malinowa Chwila"


# TEST CASES

class online_shoping_tests(unittest.TestCase):

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
        shop_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/ul/li[1]/a"))
        )
        shop_button.click()
        sleep(5)


    def tearDown(self):
        self.driver.quit()



    # TEST CASE ID 1 - REDIRECTION TO THE STORE PAGE CONFIRMATION (SHOWING AVAILABLE CATEGORIES OF PRODUCTS)

    def test_case_ID_1(self):

        # EXPECTED RESULT

        current_url_1 = self.driver.current_url
        self.assertEqual(current_url_1, shop_site_url, "Redirection to shop website succeeded!")
        print("Test Case ID 1 OK: Redirection to shop website succeeded!")



    # TEST CASE ID 2 - TESTING BASIC FUNCTIONALITIES OF ONLINE SHOPPING USING 'CBD OILS' CATEGORY

    def test_case_ID_2(self):

        CBD_oils = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > ul > li:nth-child(1) > div > a")
        CBD_oils.click()
        sleep(5)
        product_sorting_options = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > form > select")
        product_sorting_options.click()
        lowest_price = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > form > select > option:nth-child(5)")
        lowest_price.click()
        sleep(5)
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > ul > li.product.type-product.post-2319.status-publish.first.instock.product_cat-olejki-cbd-cbg.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple > div > div.ope-woo-card-footer > a")
        add_to_cart.click()
        show_cart_content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/ul/li[1]/div/div[2]/a[2]"))
        )
        show_cart_content.click()
        sleep(5)

        quantity = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
        quantity.click()
        quantity.clear()
        quantity.send_keys("2")
        update_cart = self.driver.find_element(By.CSS_SELECTOR, "#post-99 > div > div.woocommerce > form > table > tbody > tr:nth-child(2) > td > button")
        update_cart.click()
        sleep(5)

        # EXPECTED RESULT 1

        cart_update_confirmation = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/div"))
        )
        if cart_update_confirmation.is_displayed():
            print("Test Case ID 2 OK: The amount of products in cart has been successfully changed!")
        else:
            print("Test Case ID 2 FAIL: Cart update fail!")

        # EXPECTED RESULT 2

        quantity_input_field = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
        actual_product_quantity = quantity_input_field.get_attribute('value')
        actual_product_quantity = int(actual_product_quantity)

        if (actual_product_quantity) > 1:
            print("Test Case ID 2 OK: The amount of products in cart has been successfully changed!")
        else:
            print("Test Case ID 2 FAIL: Cart update fail!")



    # TEST CASE ID 3 - TESTING BASIC FUNCTIONALITIES OF ONLINE SHOPPING USING 'HEMP TEA' CATEGORY

    def test_case_ID_3(self):

        hemp_tea = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > ul > li:nth-child(3) > div > a")
        hemp_tea.click()
        sleep(5)
        italian_origin = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > ul > li:nth-child(1) > div > a")
        italian_origin.click()
        sleep(5)
        product_sorting_options = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > form > select")
        product_sorting_options.click()
        higher_price = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > form > select > option:nth-child(6)")
        higher_price.click()
        sleep(5)
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > ul > li.product.type-product.post-1347.status-publish.first.instock.product_cat-carmagnola.has-post-thumbnail.sale.shipping-taxable.purchasable.product-type-simple > div > div.ope-woo-card-footer > a")
        add_to_cart.click()
        show_cart_content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/ul/li[1]/div/div[2]/a[2]"))
        )
        show_cart_content.click()
        sleep(5)

        # EXPECTED RESULT

        quantity_input_field = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
        actual_product_quantity = quantity_input_field.get_attribute('value')
        actual_product_quantity = int(actual_product_quantity)

        if (actual_product_quantity) > 0:
            print("Test Case ID 3 OK: Product has been successfully added to the cart!")
        else:
            print("Test Case ID 3 FAIL: Cart is empty!")



    # TEST CASE ID 4 - TESTING BASIC FUNCTIONALITIES OF ONLINE SHOPPING USING 'HEMP FRUIT TEA' CATEGORY

    def test_case_ID_4(self):

        hemp_fruit_tea = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > ul > li:nth-child(7) > div > a")
        hemp_fruit_tea.click()
        sleep(5)
        product_sorting_options = self.driver.find_element(By.CSS_SELECTOR,"#page-content > div > div > div > form > select")
        product_sorting_options.click()
        most_popular = self.driver.find_element(By.CSS_SELECTOR,"#page-content > div > div > div > form > select > option:nth-child(2)")
        most_popular.click()
        sleep(5)
        malinowa_chwila = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > ul > li.product.type-product.post-2553.status-publish.first.instock.product_cat-50g.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple")
        malinowa_chwila.click()
        sleep(5)

        # EXPECTED RESULT 1

        product_description = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]"))
        )
        product_description_text = product_description.text

        if most_popular_tea_name in product_description_text:
            print("Test Case ID 4 OK: Redirection to chosen product website succeeded!")
        else:
            print("Test Case ID 4 FAIL: Redirection failed!")
        sleep(5)

        # EXPECTED RESULT 2

        add_to_cart = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div[2]/form/button"))
        )
        add_to_cart.click()

        product_successfully_added_to_cart_communicate = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div/p"))
        )

        if product_successfully_added_to_cart_communicate.is_displayed():
            print("Test Case ID 4 OK: Chosen product successfully added to the cart!")
        else:
            print("Test Case ID 4 FAIL: Product added to the cart failed!")
        sleep(5)

        # EXPECTED RESULT 3

        show_cart_content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div/a"))
        )

        show_cart_content.click()
        sleep(5)

        quantity_input_field = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
        actual_product_quantity = quantity_input_field.get_attribute('value')
        actual_product_quantity = int(actual_product_quantity)

        if (actual_product_quantity) > 0:
            print("Test Case ID 4 OK: Product has been successfully added to the cart!")
        else:
            print("Test Case ID 4 FAIL: Cart is empty!")



    # TEST CASE ID 5 - DELETING PRODUCT PREVIOUSLY ADDED TO THE CART TESTING USING 'HEMP SOAP' CATEGORY

    def test_case_ID_5(self):

        hemp_soap = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > ul > li:nth-child(10) > div")
        hemp_soap.click()
        sleep(5)
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#page-content > div > div > div > ul > li.product.type-product.post-1813.status-publish.last.instock.product_cat-decor.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple > div > div.ope-woo-card-footer > a")
        add_to_cart.click()
        show_cart_content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/ul/li[5]/div/div[2]/a[2]"))
        )
        show_cart_content.click()

        product_remove_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/form/table/tbody/tr[1]/td[1]/a"))
        )
        product_remove_button.click()
        sleep(5)

        # EXPECTED RESULT 1

        product_deleting_communicate = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]"))
        )

        if product_deleting_communicate.is_displayed():
            print("Test Case ID 5 OK: Cart content successfully deleting!")
        else:
            print("Test Case ID 5 FAIL: Deleting of cart content failed!")

        # EXPECTED RESULT 2

        empty_cart_communicate = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[1]/div[1]/div[2]"))
        )

        if empty_cart_communicate.is_displayed():
            print("Test Case ID 5 OK: Cart is empty!")
        else:
            print("Test Case ID 5 FAIL: Cart is still not empty!")



if __name__ == "__main__":
    unittest.main()
