# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Avalonlogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_avalonlogin(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_id("login_name").send_keys("ivo@digitalcube.rs")
        driver.find_element_by_id("login_pass").send_keys("123")
        # ERROR: Caught exception [Error: unknown strategy [class] for locator [class=login-button]]
        driver.find_element_by_css_selector("[class*='login-button']")
        # ERROR: Caught exception [Error: unknown strategy [class] for locator [class=content-header-main]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonEmailMistake(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_email_mistake(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_id("login_name").send_keys("ivo@digitacube.rs")
        driver.find_element_by_id("login_pass").send_keys("123")
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | css=input.login-button | ]]
        # ERROR: Caught exception [Error: unknown strategy [class] for locator [class=ng-scope]]

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonFullnNameInputError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_fulln_name_input_error(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        self.assertEqual("AVALON", driver.title)
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ab")
        self.assertTrue(
            driver.find_element_by_css_selector("div.validation-form-description.ng-binding").is_displayed())
        driver.find_element_by_id("register_back").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonEmailInputError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_email_input_error(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "login"))
        driver.find_element_by_xpath("//input[@type='email']").send_keys("abc")
        self.assertTrue(
            driver.find_element_by_css_selector("div.validation-form-description.ng-binding").is_displayed())
        driver.find_element_by_id("register_back").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonPasswordInputError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_password_input_error(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='languages']/li"))
        driver.find_element_by_xpath("//input[@type='email']").send_keys("123")
        self.assertTrue(driver.find_element_by_xpath("//input[@type='password']").is_displayed())
        driver.find_element_by_id("register_back").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonLanguage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_language(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        # ERROR: Caught exception [Error: unknown strategy [class] for locator [class=header-language ng-binding]]
        self.assertEqual("Tilmeld dig her", driver.find_element_by_link_text("Tilmeld dig her").text)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonSignupAndBack(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_signup_and_back(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_id("register_back").click()
        self.assertTrue(driver.find_element_by_css_selector("avalon-logo").is_displayed())

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity3").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("Triathlon")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:2' | ]]
        # driver.execute_script("""document.getElementById('sign-run-distance').value='number:2'""")
        # driver.manage().timeouts().implicitlyWait(30, time.SECONDS);
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[7]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[11]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[12]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register1(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity2").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("!\"#$#&%$/%/&/&%")
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("MARATON")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:15' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:4' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | id=sign-run-distance | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2047' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("sig4").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:1' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:31' | ]]
        driver.find_element_by_id("runner-background").send_keys("I am fucking CONTADOR el pisttolero")
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_id("injury-description").send_keys("break my mind")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("123131213")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("31321")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('training-session').value='number:3' | ]]
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[5]/label").click()
        driver.find_element_by_id("register_back").click()
        driver.find_element_by_id("register_back").click()
        driver.find_element_by_id("register_back").click()
        driver.find_element_by_id("register_back").click()
        driver.find_element_by_id("register_back").click()
        driver.find_element_by_id("register_back").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register2(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity4").click()
        driver.find_element_by_id("activity4-sub1").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-gss-train-level').value='number:1' | ]]
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[2]/label").click()
        driver.find_element_by_id("gss-goal-description").send_keys("AbCdEf !\"!\"%$#$&%$&(=)=+097127986241764132")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:31' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:11' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2001' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("running-state4").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("13")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('gss-runs').value='number:6' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('gss-run-duration').value='number:3' | ]]
        driver.find_element_by_id("gss-gps-access-no").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register3(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity1").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:3' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:2' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("12321314?)==)/(/&%&$,,,,,khtdkhdkhtd")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:1' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:0' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2027' | ]]
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(
            u"1234243241?=)/(=/(&(&%#$$%\"   -.,-.,.-,-đšpđšpđćčlćčlćčl")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:28' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:8' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:1965' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_id("injury-description").send_keys(
            u"125348`52/(&!(/&53465_:;_:ĆČLĆLPahsdaljhdlgljhghjgglghg")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("5")
        driver.find_element_by_xpath("(//input[@type='number'])[3]").send_keys("88")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('training-session').value='number:3' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[3]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[5]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[6]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register4(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity1").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:1' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:1' | ]]
        driver.find_element_by_xpath("//input[@type='text']").send_keys("123MNBnmb+_)+_)*(&")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("sig4").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:29' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:11' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:1984' | ]]
        driver.find_element_by_id("runner-background").send_keys("123132,jhv,ghc")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("5")
        driver.find_element_by_xpath("(//input[@type='number'])[5]").send_keys("50")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:1' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[6]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register5(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity1").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:2' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:2' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("\"!#\"!'09;JHFbvc65135")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:1' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:5' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2025' | ]]
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("s,hjgj8768761/O&%/&O$%")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("sig4").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:31' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:11' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:1911' | ]]
        driver.find_element_by_id("runner-background").send_keys("FhFkVlNlnl876786'=(=/")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("1325")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("51")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('training-session').value='number:3' | ]]

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister6(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register6(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity1").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:3' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:3' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:4' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:8' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:1944' | ]]
        driver.find_element_by_id("runner-background").send_keys(
            "kjh                                                                                                                                                                                                           sddsddssdds")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("100")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("100")
        driver.find_element_by_xpath("(//input[@type='number'])[3]").send_keys("100")
        driver.find_element_by_xpath("(//input[@type='number'])[4]").send_keys("100")
        driver.find_element_by_xpath("(//input[@type='number'])[5]").send_keys("100")
        driver.find_element_by_xpath("(//input[@type='number'])[6]").send_keys("100")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('training-session').value='number:5' | ]]
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[5]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[6]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister7(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register7(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity2").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:1' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:1' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("IUIU jb,bj\"$!#$\"!\"786896986")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:21' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:11' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2051' | ]]
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("ajkbs, :_;:_;")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:21' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:1' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2011' | ]]
        driver.find_element_by_id("runner-background").send_keys("asdadsasd21341234=)(=)(")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("78")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("84")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('training-session').value='number:2' | ]]
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[5]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[9]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[10]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister8(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register8(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity2").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:2' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:2' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("sig4").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:21' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:11' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2001' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('training-session').value='number:3' | ]]
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[5]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[10]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister9(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register9(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity2").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:3' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:3' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("PEra mika 1`23")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:7' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:2' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2047' | ]]
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("Janos kkjkj123 )(/)(")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:19' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:6' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2007' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("213213")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("7")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('training-session').value='number:5' | ]]
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[10]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[9]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister10(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register10(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity3").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:1' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:3' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:27' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:7' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2017' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_id("injury-description").send_keys("MNBMNBkjhkjhkjhk(&(/&(/6543563")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("23")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("41")
        driver.find_element_by_xpath("(//input[@type='number'])[3]").send_keys("11")
        driver.find_element_by_xpath("(//input[@type='number'])[4]").send_keys("17")
        driver.find_element_by_xpath("(//input[@type='number'])[5]").send_keys("55")
        driver.find_element_by_xpath("(//input[@type='number'])[6]").send_keys("44")
        driver.find_element_by_xpath("(//input[@type='number'])[7]").send_keys("64")
        driver.find_element_by_xpath("(//input[@type='number'])[8]").send_keys("25")
        driver.find_element_by_xpath("(//input[@type='number'])[9]").send_keys("39")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('training-hours').value='number:1' | ]]
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[11]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[12]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister11(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register11(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity3").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:2' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:2' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("sig4").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:7' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:7' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2007' | ]]
        driver.find_element_by_id("runner-background").send_keys("$# \"$# KG   H J'0 82  3mjb")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("(//input[@type='number'])[4]").send_keys("234")
        driver.find_element_by_xpath("(//input[@type='number'])[5]").send_keys("22")
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[10]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[11]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister12(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register12(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity3").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-train-level').value='number:2' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-run-distance').value='number:2' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:30' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:4' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2027' | ]]
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("s  da ; MN; MN45# %# '0980'")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_id("injury-description").send_keys("popo ooo)()())54545  vbVBVN")
        driver.find_element_by_id("runner-background").send_keys("NMBMNB (/&(/ $%$%#234")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("14")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("8")
        driver.find_element_by_xpath("(//input[@type='number'])[3]").send_keys("11")
        driver.find_element_by_xpath("(//input[@type='number'])[4]").send_keys("17")
        driver.find_element_by_xpath("(//input[@type='number'])[5]").send_keys("5")
        driver.find_element_by_xpath("(//input[@type='number'])[6]").send_keys("4")
        driver.find_element_by_xpath("(//input[@type='number'])[7]").send_keys("7")
        driver.find_element_by_xpath("(//input[@type='number'])[8]").send_keys("55")
        driver.find_element_by_xpath("(//input[@type='number'])[9]").send_keys("44")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('training-hours').value='number:1' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("(//input[@type='number'])[4]").send_keys("34")
        driver.find_element_by_xpath("(//input[@type='number'])[5]").send_keys("55")
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[11]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister13(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register13(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity4").click()
        driver.find_element_by_id("activity4-sub1").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-gss-train-level').value='number:1' | ]]
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[2]/label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[3]/label").click()
        driver.find_element_by_id("gss-goal-description").send_keys("gh  $ %#% $\"#7 '97'    87 'JGHg")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("sig4").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:30' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:4' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:1983' | ]]
        driver.find_element_by_id("gss-active-yes").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('sign-gss-activity').value='number:1' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("running-state2").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("55")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("44")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('gss-runs').value='number:6' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript |  document.getElementById('gss-run-duration').value='number:3' | ]]
        driver.find_element_by_id("gss-gps-access-no").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("gss-weight1").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("21")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:18' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:4' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:2018' | ]]
        driver.find_element_by_id("eating-habits").send_keys("kjhjks    NBVBNVB#\"#$\"$#/(=)=)45543")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("gss-strength1").click()
        driver.find_element_by_id("gss-strength-today2").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('gss-strength-trainings').value='number:2' | ]]
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[11]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister14(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register14(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity4").click()
        driver.find_element_by_id("activity4-sub2").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[2]/label").click()
        driver.find_element_by_id("gss-goal-no").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:10' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:10' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:1993' | ]]
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("gss-weight2").click()
        driver.find_element_by_id("gss-weight2").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[4]/div[2]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


class AvalonRegister15(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.rs/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_avalon_register15(self):
        driver = self.driver
        driver.get("http://avalonactive.com/login")
        driver.find_element_by_link_text("Signup here").click()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("ivan jankovic")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ivan@digitalcube.rs")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("IsJ50111")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("IsJ50111")
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("activity4").click()
        driver.find_element_by_id("activity4-sub1").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("sig4").click()
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.day')[0].value='number:30' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.month')[0].value='number:8' | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementsByName('dateFields.year')[0].value='number:1973' | ]]
        driver.find_element_by_id("gss-active-yes").click()
        driver.find_element_by_xpath("//input[@value='Next']").click()
        driver.find_element_by_id("running-state4").click()
        driver.find_element_by_xpath("//input[@type='number']").send_keys("66")
        driver.find_element_by_xpath("(//input[@type='number'])[2]").send_keys("4")
        # ERROR: Caught exception [ERROR: Unsupported command [runScript | document.getElementById('gss-run-duration').value='number:3' | ]]
        driver.find_element_by_id("gss-gps-access-no").click()
        driver.find_element_by_css_selector("div.sign_check > label").click()
        driver.find_element_by_xpath(
            "//div[@id='login-wrapper-new']/dc-login-content/div[2]/div/div/div[11]/div[2]/label").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
