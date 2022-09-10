import sys

from page_object_scooter.orderPageScooter import OrderPageCsooter

sys.path.insert(0, '/the/folder/path/page_object_scooter/')
from selenium import webdriver
from page_object_scooter.homePageScooter import HomePageCsooter
import allure


class TesttestOrderingScooter:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.set_window_size(1920, 1080)

    @allure.title ('Проверка 1 - Оформление заказа по кнопке вверху страницы (Метро: Черкизовская, Срок: 1 день, Дата: 15 сентября, цвет самоката: черный)')
    def test_order_button_top_page(self):
        order_page = OrderPageCsooter(self.driver)
        home_page = HomePageCsooter(self.driver)
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.click_order_button_at_top_page() #клик по кнопке Заказать вверху страницы
        order_page.enter_name() #ввести имя
        order_page.enter_last_name() #ввести фамилию
        order_page.enter_address() #ввести адрес
        order_page.click_metro_field() #кликнуть по селекту метро
        order_page.select_metro_station_cherkizovskaya() #выбрать станию Черкизовская
        order_page.enter_phone() #ввести телефон

        order_page.click_further_button() #клик по кнопке Далее - переход на 2 форму

        order_page.click_when_bring_scooter_select() #кликнуть по полю Когда привезти
        order_page.click_when_bring_select_fifteenth() #выбрать 15 число
        order_page.click_rental_period_select() #кликнуть по полю срок аренды
        order_page.click_rental_period_one_day() #выбрать срок аренды один день
        order_page.click_color_scooter_black_check_box() #выбрать черный цвет самоката
        order_page.enter_comment() #оставить комментарий курьеру

        order_page.click_order_button() #клик по кнопке Заказать

        order_page.click_yes_button() #клик по кнопке Да

        assert order_page.viewStatusButton #ОР: появилась кнопка Посмотреть статус

    @allure.title('Проверка 2 - Оформление заказа по кнопке внизу страницы (Метро: Красносельская, Срок: 2 дня, Дата: 30 сентября, Цвет самоката: серый)')
    def test_order_button_down_page(self):
        order_page = OrderPageCsooter(self.driver)
        home_page = HomePageCsooter(self.driver)
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page.wait()
        home_page.scroll_order_button()  # проскроллить до кнопки Заказать
        home_page.wait()
        home_page.click_order_button_at_down_page()  # клик по кнопке Заказать внизу страницы

        order_page.enter_name()  # ввести имя
        order_page.enter_last_name()  # ввести фамилию
        order_page.enter_address()  # ввести адрес
        order_page.click_metro_field()  # кликнуть по селекту метро
        order_page.select_metro_station_krasnoselskaya()  # выбрать станию Красносельская
        order_page.enter_phone()  # ввести телефон

        order_page.click_further_button()  # клик по кнопке Далее - переход на 2 форму

        order_page.click_when_bring_scooter_select()  # кликнуть по полю Когда привезти
        order_page.click_when_bring_select_thirtieth()  # выбрать 30 число
        order_page.click_rental_period_select()  # кликнуть по полю срок аренды
        order_page.click_rental_period_two_days()  # выбрать срок аренды два дня
        order_page.click_color_scooter_grey_check_box()  # выбрать серый цвет самоката
        order_page.enter_comment()  # оставить комментарий курьеру

        order_page.click_order_button()  # клик по кнопке Заказать

        order_page.click_yes_button()  # клик по кнопке Да

        assert order_page.viewStatusButton  # ОР: появилась кнопка Посмотреть статус

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()