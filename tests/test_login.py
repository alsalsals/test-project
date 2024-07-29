from selene import have
from test_project.pages.login_page import LoginPage
from test_project.pages.start_page import StartPage


def test_login_with_incorrect_temporary_code():
    '''
    Тест проверяет процесс входа с неправильными данными (некорректный временный код).
    '''

    start_page = StartPage()
    login_page = LoginPage()

    start_page.open()
    start_page.login_button_click()
    login_page.type_login('login@gmail.com')

    login_page.submit_button_click()
    login_page.type_temporary_code()
    login_page.continue_button_click()

    login_page.error_message_text.should(have.text('The code is incorrect. Try again'))




