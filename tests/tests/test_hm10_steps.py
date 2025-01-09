import allure
from selene import have
from selene.support.shared import browser


def test_bank_page():
    open_bank_page()
    choose_login_type()
    choose_login_user()
    check_the_field_account()


@allure.step("Открываем страницу")
def open_bank_page():
    browser.open('')

@allure.step("Выбираем тип пользователя: customer")
def choose_login_type():
    browser.element('[ng-click="customer()"]').click()

@allure.step("Выбираем пользователя")
def choose_login_user():
    browser.element('[id="userSelect"]').click()
    browser.element('[id="userSelect"]').element('[value="1"]').click()
    browser.element('[type="submit"]').click()

@allure.step("Проверяем отображение параметра account")
def check_the_field_account():
    browser.element('.center').should(have.text('Account Number : '))