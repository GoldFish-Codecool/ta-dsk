import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPractice:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_exercise_1(self):
        self.driver.get("https://web.archive.org/web/20180926132852/http://www.seleniumeasy.com/test/basic-first-form-demo.html")
        time.sleep(3)

    def test_exercise_2(self):
        self.driver.get("https://web.archive.org/web/20180902061717/http://www.seleniumeasy.com/test/basic-first-form-demo.html")
        text = "Hello"
        user_message_input = self.driver.find_element(By.ID, "user-message")
        user_message_input.send_keys(text)
        button_show_message = self.driver.find_element(By.XPATH, "//button[normalize-space()='Show Message']")
        button_show_message.click()
        user_message_display = self.driver.find_element(By.ID, "display")
        assert text == user_message_display.text

    def test_exercise_3(self):
        self.driver.get("https://web.archive.org/web/20180902061717/http://www.seleniumeasy.com/test/basic-first-form-demo.html")
        number_a = 6
        number_b = 8
        number_a_input = self.driver.find_element(By.ID, "sum1")
        number_a_input.send_keys(str(number_a))
        number_b_input = self.driver.find_element(By.ID, "sum2")
        number_b_input.send_keys(str(number_b))
        button_show_message = self.driver.find_element(By.XPATH, "//button[normalize-space()='Get Total']")
        button_show_message.click()
        sum_display = self.driver.find_element(By.ID, "displayvalue")
        assert str(number_a + number_b) == sum_display.text

    def test_exercise_3_large(self):
        self.driver.get("https://web.archive.org/web/20180902061717/http://www.seleniumeasy.com/test/basic-first-form-demo.html")
        number_a = 1234567890
        number_b = 2345678901
        number_a_input = self.driver.find_element(By.ID, "sum1")
        number_a_input.send_keys(str(number_a))
        number_b_input = self.driver.find_element(By.ID, "sum2")
        number_b_input.send_keys(str(number_b))
        button_show_message = self.driver.find_element(By.XPATH, "//button[normalize-space()='Get Total']")
        button_show_message.click()
        sum_display = self.driver.find_element(By.ID, "displayvalue")
        assert str(number_a + number_b) == sum_display.text

    def test_exercise_4_single_checkbox(self):
        self.driver.get("https://web.archive.org/web/20180902061717/http://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        checkbox_input = self.driver.find_element(By.ID, "isAgeSelected")
        checkbox_input.click()
        checkbox_display = self.driver.find_element(By.ID, "txtAge")
        assert "Success - Check box is checked" == checkbox_display.text

    def test_exercise_4_multiple_checkbox_positive(self):
        self.driver.get("https://web.archive.org/web/20180902061717/http://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        check_all_button = self.driver.find_element(By.XPATH, "//input[@id='check1']")
        check_all_button.click()
        first_checkbox = self.driver.find_element(By.XPATH, "//label[normalize-space()='Option 1']//input[@type='checkbox']")

        assert first_checkbox.is_selected()

    def test_exercise_4_multiple_checkbox_negative(self):
        self.driver.get("https://web.archive.org/web/20180902061717/http://www.seleniumeasy.com/test/basic-checkbox-demo.html")

        checkbox_01 = self.driver.find_element(By.XPATH, "//label[normalize-space()='Option 1']")
        checkbox_02 = self.driver.find_element(By.XPATH, "//label[normalize-space()='Option 2']")
        checkbox_03 = self.driver.find_element(By.XPATH, "//label[normalize-space()='Option 3']")

        checkbox_01.click()
        checkbox_02.click()
        checkbox_03.click()

        check_all_button = self.driver.find_element(By.XPATH, "//input[@id='check1']")

        assert check_all_button.get_attribute("value") == "Uncheck All" # is should be "Check All", since we only checked 3 of the checkboxes

    def test_exercise_5_select(self):
        self.driver.get("https://web.archive.org/web/20180820002117/http://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

        day = "Monday"

        select_element_day = self.driver.find_element(By.XPATH, "//select[@id='select-demo']")
        select_day = Select(select_element_day)
        select_day.select_by_visible_text(day)

        select_day_display = self.driver.find_element(By.XPATH, "//p[@class='selected-value']")

        assert select_day_display.text == f"Day selected :- {day}"

    def test_exercise_6_radio_buttons(self):
        self.driver.get("https://web.archive.org/web/20180817001806/http://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

        male_radio_button = self.driver.find_element(By.XPATH, "//label[normalize-space()='Male']//input[@name='gender']")
        male_radio_button.click()
        age_15_50_radio_button = self.driver.find_element(By.XPATH, "//input[@value='15 - 50']")
        age_15_50_radio_button.click()

        button_get_values = self.driver.find_element(By.XPATH, "//button[normalize-space()='Get values']")
        button_get_values.click()

        result_display = self.driver.find_element(By.XPATH, "//p[@class='groupradiobutton']")

        assert result_display.text == "Sex : Male\nAge group: 15 - 50"