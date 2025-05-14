from time import sleep

from selene import browser, be, have

def test_positive_search(test_open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Selene'))

def test_negative_search(test_open_browser):
    browser.element('[name="q"]').should(be.blank).type('84не934рпгшкпгукпгшуне73485346347856485247кпауропава').press_enter()
    browser.element('html').should(have.text('No results found for'))
