import allure
from selene import have
from selene.support.shared import browser


def test_search_with_steps():
    with allure.step("Открываем браузер"):
        browser.open('')

    with allure.step("Вводим значение в поисковую строку"):
        browser.element('[name="q"]').type('вишня').press_enter()

    with allure.step("Проверяем наличие заголовка 'Растение'"):
        browser.element('[data-attrid="subtitle"]').should(have.text('Растене'))


def test_search_with_decorator_steps():
    open_page()
    fill_the_search_field("вишня")
    check_the_name_of_field("Растение")


@allure.step("Открываем браузер")
def open_page():
    browser.open('')


@allure.step("Вводим значение {word} в поисковую строку")
def fill_the_search_field(word):
    browser.element('[name="q"]').type(word).press_enter()


@allure.step("Проверяем наличие заголовка {title}")
def check_the_name_of_field(title):
    browser.element('[data-attrid="subtitle"]').should(have.text(title))
