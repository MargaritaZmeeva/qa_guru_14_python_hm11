import allure
from selene import have
from selene.support.shared import browser


def test_bank_page_with_steps():
    with allure.step("Открываем страницу"):
        browser.open('')

    with allure.step("Выбираем тип пользователя: customer"):
        browser.element('[ng-click="customer()"]').click()

    with allure.step("Выбираем пользователя"):
        browser.element('[id="userSelect"]').click()
        browser.element('[id="userSelect"]').element('[value="1"]').click()
        browser.element('[type="submit"]').click()

    with allure.step("Проверяем отображение параметра account"):
        browser.element('.center').should(have.text('Account Number : '))

