import time

import pytest

from Utilities.Logger import LogGenerator
from Utilities.redconfigFile import ReadConfigfile
from pageObjects.LoginPage import Test_Login


@pytest.mark.usefixtures("startup")
class Test_Login001:
    Username = ReadConfigfile.getUsername()
    Password = ReadConfigfile.getPassword()
    username = ReadConfigfile.username()
    password = ReadConfigfile.password()
    log = LogGenerator.loggen()

    @pytest.mark.G1
    def test_Page(self, startup):
        self.driver = startup
        self.TP = Test_Login(self.driver)
        self.TP.test_Username(self.Username)
        self.log.info("Username --->" + self.Username)
        print("\n Username --->" + self.Username)
        time.sleep(2)
        self.TP.test_Password(self.Password)
        self.log.info("Password --->" + self.Password)
        print("\n Password --->" + self.Password)
        time.sleep(2)
        print("\n The Web Title --->" + self.driver.title)
        self.log.info("The Web Title")
        self.TP.test_Login()
        if self.driver.title not in "Login Pass":
            self.log.info("screenshot pass")
            self.driver.save_screenshot("..\\Demoproject\\screenshot\\test_Login_Pass.png")
            assert True
            self.driver.quit()
        else:
            self.log.info("screenshot Fail")
            self.driver.save_screenshot("..\\Demoproject\\screenshot\\test_Login_Fail.png")
            assert False

    @pytest.mark.G2
    def test_Page_First(self, startup):
        self.driver = startup
        self.TP2 = Test_Login(self.driver)
        self.TP2.test_Username(self.Username)
        self.log.info("Username --->" + self.Username)
        print("\n Username --->" + self.Username)
        time.sleep(2)
        self.TP2.test_Password(self.Password)
        self.log.info("Password --->" + self.Password)
        print("\n Password --->" + self.Password)
        time.sleep(2)
        self.log.info("The Web Title")
        self.TP2.test_Login()
        time.sleep(2)
        self.TP2.test_Add_to_cart_First()
        self.TP2.test_Add_to_card_second()
        self.log.info("test_Add_to_card_second")
        self.TP2.test_Add_to_third()
        self.log.info("test_Add_to_third")
        time.sleep(2)
        self.TP2.test_shop()
        self.log.info("test_shop")
        self.TP2.test_checkout()
        self.log.info("test_checkout")
        time.sleep(2)
        self.TP2.test_First_name()
        self.log.info("test_First_name")
        self.TP2.test_Last_name()
        self.log.info("test_Last_name")
        self.TP2.test_zip()
        self.log.info("test_zip")
        time.sleep(2)
        self.TP2.test_button()
        self.log.info("test_button")
        self.TP2.test_Finish()
        self.log.info("test_Finish")
        if self.TP2.test_Finish_XAPTH() not in "Finish":
            self.log.info("Testcase Pass")
            self.driver.save_screenshot(r"C:\Users\ajayj\PycharmProjects\practive_framework_03\Demoproject\screenshot\Test_Page2_Pass.png")
            assert True
            self.driver.quit()
        else:
            self.log.info("Testcase Fail")
            self.driver.save_screenshot(r"C:\Users\ajayj\PycharmProjects\practive_framework_03\Demoproject\screenshot\Test_Page2_Fail.png")
            assert False

    @pytest.mark.G3
    def test_Page3(self, startup, DataForLogin):
        self.driver = startup
        self.TP3 = Test_Login(self.driver)
        self.TP3.test_Username(DataForLogin[0])
        self.log.info("Username --->" + DataForLogin[0])
        print("\n Username --->" + DataForLogin[0])
        time.sleep(2)
        self.TP3.test_Password(DataForLogin[1])
        self.log.info("Password --->" + DataForLogin[1])
        print("\n Password --->" + DataForLogin[1])
        time.sleep(2)
        Testcase_status_list = []
        self.log.info("The Web Title")
        self.TP3.test_Login()
        if self.TP3.test_click_Button() == "Login Pass":
            # Testcase_status_list.append("Pass")
            if self.TP3.test_Logout() == "Login Pass":
                self.log.info("Testcase is pass")
                print('Testcase is Pass')
                time.sleep(5)
                if DataForLogin[2] == "Fail":
                    Testcase_status_list.append("Pass")
                    # self.driver.save_screenshot("..\\Demoproject\\screenshot\\TestPage3_Pass.png")
                    self.log.info("Take screenshot")
                    time.sleep(1)
                    self.TP3.test_Login()
                    self.TP3.test_click_Button()
                    self.driver.save_screenshot("C:\\Users\\ajayj\\PycharmProjects\\practive_framework_03\\Demoproject\\screenshot\\TestPage3_Pass.png")
                    self.TP3.test_Logout()
                    self.driver.quit()
                elif DataForLogin[2] == "Pass":
                    Testcase_status_list.append("Pass")
                    # self.driver.save_screenshot("..\\Demoproject\\screenshot\\Test_Page3_Pass.png")
                    self.log.info("Take screenshot")
                    self.TP3.test_Login()
                    self.log.info("Click Button")
                    self.TP3.test_click_Button()
                    self.driver.save_screenshot("C:\\Users\\ajayj\\PycharmProjects\\practive_framework_03\\Demoproject\\screenshot\\Test_Page3_Pass.png")
                    self.TP3.test_Logout()
                    self.log.info("Click Logout")
                    self.driver.quit()
            elif self.TP3.test_click_Button() == "Login Fail":
                self.log.info("Testcase is Fail")
                print('Testcase is Fail')
                if DataForLogin[2] == "Fail":
                    Testcase_status_list.append("Pass")
                    self.driver.save_screenshot("C:\\Users\\ajayj\\PycharmProjects\\practive_framework_03\\Demoproject\\screenshot\\Test_Page3_Pass.png")
                    self.log.info("Take screenshot")
                    self.driver.quit()
                elif DataForLogin[2] == "Pass":
                    Testcase_status_list.append("Fail")
                    self.driver.save_screenshot("C:\\Users\\ajayj\\PycharmProjects\\practive_framework_03\\Demoproject\\screenshot\\Test_Page3_Fail.png")
                    self.log.info("Take screenshot")
                    self.driver.quit()
            print(Testcase_status_list)
            for i in Testcase_status_list:
                if i not in "Pass":
                    time.sleep(2)
                    self.log.info("Test_case test_user_login_Params_004 is Passed")
                    print("Testcase is Pass")
                    assert True
                else:
                    print("Testcase is Fail")
                    time.sleep(2)
                    self.log.info("Test_case test_user_login_Params_004 is Failed")
                    assert False
        self.log.info("Test_case test_user_login param_004 is Completed")

