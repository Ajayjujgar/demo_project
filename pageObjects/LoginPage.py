from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_Login:
    Username_XPATH = "//*[@id='user-name']"
    Password_XPATH = '//*[@id="password"]'
    Login_XPATH = '//*[@id="login-button"]'
    Add_to_cart_First = "//*[text()='Add to cart']"
    Add_to_cart_second = "//*[text()='Add to cart']"
    Add_to_cart_Third = "//*[text()='Add to cart']"
    shop = '//*[@id="shopping_cart_container"]'
    checkout = '//*[@id="checkout"]'
    test_title = "//*[text()='Swag Labs']"
    First_name = '//*[@id="first-name"]'
    Last_Name = '//*[@id="last-name"]'
    Zip = '//*[@id="postal-code"]'
    button = '//*[@id="continue"]'
    Finish = '//*[@id="finish"]'
    finish_XPATH = "//*[text()='Finish']"
    click = "//*[text() ='Open Menu']"
    Logout = "//*[text() ='Logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def test_Username(self, Username):
        self.driver.find_element(By.XPATH, self.Username_XPATH).send_keys(Username)

    def test_Password(self, Password):
        self.driver.find_element(By.XPATH, self.Password_XPATH).send_keys(Password)

    def test_Login(self):
        self.driver.find_element(By.XPATH, self.Login_XPATH).click()

    def test_Add_to_cart_First(self):
        self.driver.find_element(By.XPATH, self.Add_to_cart_First).click()

    def test_Add_to_card_second(self):
        self.driver.find_element(By.XPATH, self.Add_to_cart_second).click()

    def test_Add_to_third(self):
        self.driver.find_element(By.XPATH, self.Add_to_cart_Third).click()

    def test_shop(self):
        self.driver.find_element(By.XPATH, self.shop).click()

    def test_checkout(self):
        self.driver.find_element(By.XPATH, self.checkout).click()

    def test_titles(self):
        try:
            self.driver.find_element(By.XPATH, self.test_title)
            return "Login Pass"
        except:
            return "Login Fail"

    def test_First_name(self):
        self.driver.find_element(By.XPATH, self.First_name).send_keys('John')

    def test_Last_name(self):
        self.driver.find_element(By.XPATH, self.Last_Name).send_keys("Cena")

    def test_zip(self):
        self.driver.find_element(By.XPATH, self.Zip).send_keys("463431")

    def test_button(self):
        self.driver.find_element(By.XPATH, self.button).click()

    def test_Finish(self):
        self.driver.find_element(By.XPATH, self.Finish).click()

    def test_Finish_XAPTH(self):
        try:
            self.driver.find_element(By.XPATH, self.finish_XPATH).click()
            return "Login pass"
        except:
            return "Login Fail"

    def test_click_Button(self):
        try:
            self.driver.find_element(By.XPATH, self.click).click()
            return "Login Pass"
        except:
            return "Login Fail"

    def test_Logout(self):
        try:
            self.driver.find_element(By.XPATH, self.Logout).click()
            return "Login Pass"
        except:
            return "Login Fail"
