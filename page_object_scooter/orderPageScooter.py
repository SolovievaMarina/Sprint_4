from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# инициализировали драйвер
driver = webdriver.Firefox()

class OrderPageCsooter:
    # локаторы для первой формы заказа
    nameField = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/input[1]"] #поле Имя
    lastNameField = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[2]/input[1]"] #поле Фамилия
    addressField = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[3]/input[1]"] #поле Адрес
    metroStationField = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/input[1]"] #селект выбор метро
    metroStationCherkizovskaya = [By.XPATH, ".//div[@class='select-search__select']/ul/li[2]"]
    metroStationKrasnoselskaya = [By.XPATH, ".//div[@class='select-search__select']/ul/li[5]"]

    phoneField = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[5]/input[1]"] #поле телефон

    whenBringScooterSelect = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]"] #селект Когда привезти
    whenToBringSelectFifteenth = [By.XPATH, "//div[contains(text(),'15')]"]  # 15 число
    whenToBringSelectThirtieth = [By.XPATH, "//div[contains(text(),'30')]"]  # 30 число

    rentalPeriodSelect = [By.XPATH, "//div[contains(text(),'* Срок аренды')]"] #селект Срок аренды
    rentalPeriodOneDayItem = [By.XPATH, "//div[contains(text(),'сутки')]"]
    rentalPeriodTwoDaysItem = [By.XPATH, "//div[contains(text(),'двое суток')]"]

    colorScooterBlackCheckBox = [By.XPATH, "//input[@id='black']"] #селект выбор цвета
    colorScooterGreyCheckBox = [By.XPATH, "//input[@id='grey']"]

    commentForCourierField = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[4]/input[1]"] #поле комментарий курьеру

    furtherButton = [By.XPATH, "//button[contains(text(),'Далее')]"] #кнопка Далее
    orderButton = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/button[2]"] #кнопка заказать

    modalWindowOrder = [By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[5]"] #модальное окно Хотите оформить заказ?
    yesButton = [By.XPATH, "//button[contains(text(),'Да')]"] #кнопка Да

    viewStatusButton = [By.XPATH, "//button[contains(text(),'Посмотреть статус')]"] #кнопка Посмотреть статус


    def __init__(self, driver):
        self.driver = driver

    # заполнение первой формы
    def enter_name(self):
        self.driver.find_element(*self.nameField).send_keys("Иван")

    def enter_last_name(self):
        self.driver.find_element(*self.lastNameField).send_keys("Иванов")

    def enter_address(self):
        self.driver.find_element(*self.addressField). send_keys("г Москва")

    def click_metro_field(self):
        self.driver.find_element(*self.metroStationField).click()

    def select_metro_station_cherkizovskaya(self):
        self.driver.find_element(*self.metroStationCherkizovskaya).click()

    def select_metro_station_krasnoselskaya(self):
        self.driver.find_element(*self.metroStationKrasnoselskaya).click()

    def enter_phone(self):
        self.driver.find_element(*self.phoneField).send_keys("+79999999999")

    # кликнуть Далее
    def click_further_button(self):
        self.driver.find_element(*self.furtherButton).click()

    # заполнение второй формы
    def click_when_bring_scooter_select(self): #клик по полю Когда привезти
        self.driver.find_element(*self.whenBringScooterSelect).click()

    def click_when_bring_select_fifteenth(self):
        self.driver.find_element(*self.whenToBringSelectFifteenth).click() #выбрать 15-е число

    def click_when_bring_select_thirtieth(self):
        self.driver.find_element(*self.whenToBringSelectThirtieth).click() #выбрать 30-е число

    def click_rental_period_select(self):
        self.driver.find_element(*self.rentalPeriodSelect).click()  #клик по полю срок аренды

    def click_rental_period_one_day(self):
        self.driver.find_element(*self.rentalPeriodOneDayItem).click()  #выбрать срок аренды 1 сутки

    def click_rental_period_two_days(self):
        self.driver.find_element(*self.rentalPeriodTwoDaysItem).click()  #выбрать срок аренды 2 суток

    def click_color_scooter_black_check_box(self):
        self.driver.find_element(*self.colorScooterBlackCheckBox).click() #выбрать цвет: черный

    def click_color_scooter_grey_check_box(self):
        self.driver.find_element(*self.colorScooterGreyCheckBox).click() #выбрать цвет: серый

    def enter_comment(self):
        self.driver.find_element(*self.commentForCourierField).send_keys("Поскорее, пожалуйста") #оставить комментарий курьеру

    def click_order_button(self):
        self.driver.find_element(*self.orderButton).click() #кликнуть Заказать

    def click_yes_button(self):
        self.driver.find_element(*self.yesButton).click() #кликнуть Да
