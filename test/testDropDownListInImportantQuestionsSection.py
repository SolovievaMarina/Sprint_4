import sys
sys.path.insert(0, '/the/folder/path/page_object_scooter/')
from selenium import webdriver
from page_object_scooter.homePageScooter import HomePageCsooter
import allure


class TestDropDownListInImportantQuestionsSection:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.set_window_size(1920, 1080)

    @allure.title('Проверка, что при нажатии на вопрос 1 "Сколько это стоит? И как оплатить?", появляется ответ')
    def test_click_question_how_much(self):
        home_page = HomePageCsooter(self.driver)
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.scroll_last_question()
        home_page.wait_for_question_how_much()
        home_page.click_question_how_much()

        assert home_page.answerToQuestionHowMuch

    @allure.title('Проверка, что при нажатии на вопрос 2 "Хочу сразу несколько самокатов! Так можно?", появляется ответ')
    def test_click_question_want_some_scooters(self):
        home_page = HomePageCsooter(self.driver)
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.scroll_last_question()
        home_page.wait_for_question_want_some_scooters()
        home_page.click_question_want_some_scooters()

        assert home_page.answerToQuestionWantSomeScooters

    @allure.title('Проверка, что при нажатии на вопрос 3 "Как рассчитывается время аренды?", появляется ответ')
    def test_click_question_how_time_calculated(self):
        home_page = HomePageCsooter(self.driver)
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.scroll_last_question()
        home_page.wait_for_question_how_time_calculated()
        home_page.click_question_how_time_calculated()

        assert home_page.answerToQuestionHowTimeCalculated

    @allure.title('Проверка, что при нажатии на вопрос 4 "Можно ли заказать самокат прямо на сегодня?", появляется ответ')
    def test_click_question_can_order_today(self):
        home_page = HomePageCsooter(self.driver)
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.scroll_last_question()
        home_page.wait_for_question_can_order_today()
        home_page.click_question_can_order_today()

        assert home_page.answerToQuestionCanOrderToday

    @allure.title('Проверка, что при нажатии на вопрос 5 "Можно ли продлить заказ или вернуть самокат раньше?", появляется ответ')
    def test_click_question_possible_to_extend(self):
        home_page = HomePageCsooter(self.driver)
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.scroll_last_question()
        home_page.wait_for_question_possible_to_extend()
        home_page.click_question_possible_to_extend()

        assert home_page.answerToQuestionPossibleToExtend

    @allure.title(
        'Проверка, что при нажатии на вопрос 6 "Вы привозите зарядку вместе с самокатом?", появляется ответ')
    def test_click_question_bringing_a_charger(self):
        home_page = HomePageCsooter(self.driver)  # создали объект класса
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.scroll_last_question()
        home_page.wait_for_question_bringing_a_charger()
        home_page.click_question_bringing_a_charger()

        assert home_page.answerToQuestionBringingACharger

    @allure.title(
        'Проверка, что при нажатии на вопрос 7 "Можно ли отменить заказ?", появляется ответ')
    def test_click_question_possible_cancel_order(self):
        home_page = HomePageCsooter(self.driver)  # создали объект класса
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.scroll_last_question()
        home_page.wait_for_question_possible_cancel_order()
        home_page.click_question_possible_cancel_order()

        assert home_page.answerToQuestionPossibleCancelOrder

    @allure.title(
        'Проверка, что при нажатии на вопрос 8 "Я живу за МКАДом, привезёте?", появляется ответ')
    def test_click_question_live_across_the_mkad(self):
        home_page = HomePageCsooter(self.driver)  # создали объект класса
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.scroll_last_question()
        home_page.wait_for_question_live_across_the_mkad()
        home_page.click_question_live_across_the_mkad()

        assert home_page.answerToQuestionLiveAcrossTheMkad

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
