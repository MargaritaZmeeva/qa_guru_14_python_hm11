from selene import have, by, be
from selene.support.shared import browser


def test_search():
    browser.open('')
    browser.element('[name="q"]').type('вишня').press_enter()
    browser.element('[data-attrid="subtitle"]').should(have.text('Растение'))


