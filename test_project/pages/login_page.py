from selene import browser


class LoginPage:
    def __init__(self):
        self.login_input = browser.element('input[inputmode="email"]')
        self.submit_button = browser.element('button[type="submit"]')
        self.temporary_code_input = browser.element('input[inputmode="numeric"]')
        self.continue_button = browser.element('button[type="submit"]')
        self.error_message_text = browser.all('form div p[font-family="Inter"]').element(1)

    def type_login(self, value):
        self.login_input.type(value)

    def submit_button_click(self):
        self.submit_button.click()

    def type_temporary_code(self):
        self.temporary_code_input.type('0000')

    def continue_button_click(self):
        self.continue_button.click()


