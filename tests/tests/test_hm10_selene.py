import allure
from selene import have
from selene.support.shared import browser


def test_bank_without_steps():

    browser.open('')
    browser.element('[ng-click="customer()"]').click()
    browser.element('[id="userSelect"]').click()
    browser.element('[id="userSelect"]').element('[value="1"]').click()
    browser.element('[type="submit"]').click()
    browser.element('.center').should(have.text('Account Number : '))

