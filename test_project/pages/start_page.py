from selene import browser


class StartPage:
    def __init__(self):
        self.login_button = browser.element('[class*="Header_button"] button')

    @staticmethod
    def open():
        browser.open('https://evvve.net/')

    def login_button_click(self):
        self.login_button.click()





