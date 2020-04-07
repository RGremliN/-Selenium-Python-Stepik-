import pytest
import time
import math

from selenium import webdriver

string = "Secret string: "

@pytest.mark.parametrize('task_id', [ "236898", "236899", "236905" ]) #"236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"  
class TestQuizField(object):

    def test_enter_correct_answer_in_filed(self, task_id, browser):

            link = f"https://stepik.org/lesson/{task_id}/step/1"

            browser.get(link)

            quiz_field = browser.find_element_by_css_selector(".string-quiz__textarea")
            answer = str(math.log(int(time.time())))
            quiz_field.send_keys(answer)

            browser.find_element_by_css_selector(".submit-submission").click()

            hint_text = browser.find_element_by_css_selector(".smart-hints__hint").text

            assert "Correct!" == hint_text, string + hint_text


