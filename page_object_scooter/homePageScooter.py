from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# инициализировали драйвер
driver = webdriver.Firefox()

class HomePageCsooter:
    #локаторы для кнопок Заказать
    orderButtonAtTopPage = [By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[2]/button[1]"]
    orderButtonAtDownPage = [By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[5]/button[1]"]

    #локаторы для FAQ (вопросы и ответы после нажатия на вопрос)
    questionHowMuch = [By.XPATH, "//div[@id='accordion__heading-0']"]
    answerToQuestionHowMuch = [By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]"]

    questionWantSomeScooters = [By.XPATH, "//div[@id='accordion__heading-1']"]
    answerToQuestionWantSomeScooters = [By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Есл')]"]

    questionHowTimeCalculated = [By.XPATH, "//div[@id='accordion__heading-2']"]
    answerToQuestionHowTimeCalculated = [By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привози')]"]

    questionCanOrderToday = [By.XPATH, "//div[@id='accordion__heading-3']"]
    answerToQuestionCanOrderToday = [By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем ')]"]

    questionPossibleToExtend = [By.XPATH, "//div[@id='accordion__heading-4']"]
    answerToQuestionPossibleToExtend = [By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можн')]"]

    questionBringingACharger = [By.XPATH, "//div[@id='accordion__heading-5']"]
    answerToQuestionBringingACharger = [By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого х')]"]

    guestionPossibleCancelOrder = [By.XPATH, "//div[@id='accordion__heading-6']"]
    answerToQuestionPossibleCancelOrder = [By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объ')]"]

    guestionLiveAcrossTheMkad = [By.XPATH, "//div[@id='accordion__heading-7']"]
    answerToQuestionLiveAcrossTheMkad = [By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Моско')]"]


    def __init__(self, driver):
        self.driver = driver

    # клик по кнопкам Заказать вверху и внизу экрана
    def click_order_button_at_top_page(self):
        self.driver.find_element(*self.orderButtonAtTopPage).click()

    def click_order_button_at_down_page(self):
        self.driver.find_element(*self.orderButtonAtDownPage).click()


    # клики по всем вопросам

    def click_question_how_much(self):
        self.driver.find_element(*self.questionHowMuch).click()

    def click_question_want_some_scooters(self):
        self.driver.find_element(*self.questionWantSomeScooters).click()

    def click_question_how_time_calculated(self):
        self.driver.find_element(*self.questionHowTimeCalculated).click()

    def click_question_can_order_today(self):
        self.driver.find_element(*self.questionCanOrderToday).click()

    def click_question_possible_to_extend(self):
        self.driver.find_element(*self.questionPossibleToExtend).click()

    def click_question_bringing_a_charger(self):
        self.driver.find_element(*self.questionBringingACharger).click()

    def click_question_possible_cancel_order(self):
        self.driver.find_element(*self.guestionPossibleCancelOrder).click()

    def click_question_live_across_the_mkad(self):
        self.driver.find_element(*self.guestionLiveAcrossTheMkad).click()


    # скролл страницы до последнего вопроса

    def scroll_last_question(self):
        element = self.driver.find_element(By.XPATH, "//div[@id='accordion__heading-7']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # скролл страницы до кнопки заказать

    def scroll_order_button(self):
        element = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[4]/div[2]/div[5]/button[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    # ожидание появления вопросов
    def wait(self):
        WebDriverWait(self.driver, 5)

    def wait_for_question_how_much(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.questionHowMuch))

    def wait_for_question_want_some_scooters(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.questionWantSomeScooters))

    def wait_for_question_how_time_calculated(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.questionHowTimeCalculated))

    def wait_for_question_can_order_today(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.questionCanOrderToday))

    def wait_for_question_possible_to_extend(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.questionPossibleToExtend))

    def wait_for_question_bringing_a_charger(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.questionBringingACharger))

    def wait_for_question_possible_cancel_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.guestionPossibleCancelOrder))

    def wait_for_question_live_across_the_mkad(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.guestionLiveAcrossTheMkad))
