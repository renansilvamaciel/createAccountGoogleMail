from webdriver_manager.chrome import ChromeDriverManager
from botcity.web.util import element_as_select
from botcity.web import WebBot, By
import pandas as pd
import random
import sys


def read_csv(file_path: str) -> pd.DataFrame:
    """
    Read csv file and return a list of data
    :param file_path:
    :return: list of data
    """
    try:

        df_employes = pd.read_csv(file_path)
        return df_employes

    except Exception as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        raise ValueError(str(error), exc_traceback.tb_lineno, exc_traceback.tb_frame.f_code.co_name)


def open_google(bot: WebBot):

    try:
        # Driver do no navegador
        bot.driver_path = ChromeDriverManager().install()

        # Acessa o site do google na pagina para criar conta
        bot.browse("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        bot.maximize_window()

    except Exception as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        raise ValueError(str(error), exc_traceback.tb_lineno, exc_traceback.tb_frame.f_code.co_name)


def account_input_name(bot: WebBot, full_name: str):

    try:
        name = full_name.split(' ')

        # Preencher nome
        bot.find_element("//input[@id='firstName']", By.XPATH, ensure_visible=True, ensure_clickable=True).send_keys(name[0])
        # sobrenome
        bot.find_element("//input[@id='lastName']", By.XPATH, ensure_visible=True, ensure_clickable=True).send_keys(name[2])
        # clica em próximo
        bot.find_element("//span[text()='Próxima']", By.XPATH, ensure_visible=True, ensure_clickable=True).click()

        # validar carregamento da próxima página:
        if not bot.find_element("//select[@id='gender']", By.XPATH, waiting_time=30000):  # espera 30 segundos
            raise Exception("Falha ao carregar a proxima pagina")

    except Exception as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        raise ValueError(str(error), exc_traceback.tb_lineno, exc_traceback.tb_frame.f_code.co_name)


def account_input_age_gender(bot: WebBot, genero: str):

        try:
            # Preencher idade
            bot.find_element("//input[@id='day']", By.XPATH, ensure_visible=True, ensure_clickable=True).send_keys('26')  # Dia
            element_as_select(bot.find_element("//select[@id='month']", By.XPATH, ensure_visible=True, ensure_clickable=True)).select_by_visible_text('Janeiro')  # Mês
            bot.find_element("//input[@id='year']", By.XPATH, ensure_visible=True, ensure_clickable=True).send_keys('1995')  # Ano

            # Selecionar gênero
            element_as_select(bot.find_element("//select[@id='gender']", By.XPATH, ensure_visible=True, ensure_clickable=True)).select_by_visible_text(genero)

            # clica em próximo
            bot.find_element("//span[text()='Próxima']", By.XPATH, ensure_visible=True, ensure_clickable=True).click()

            # validar carregamento da próxima página:
            if not bot.find_element("//input[@name='Username']", By.XPATH, waiting_time=30000):  # espera até 30 segundos
                raise Exception("Falha ao carregar a proxima pagina")

        except Exception as error:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise ValueError(str(error), exc_traceback.tb_lineno, exc_traceback.tb_frame.f_code.co_name)


def account_username(bot: WebBot, full_name):

    try:
        # Settings das variaveis
        number_aleatory = random.randint(1000, 100000)
        full_name = full_name.replace(' ', '.')

        # Preencher nome de usuário
        bot.find_element("//input[@name='Username']", By.XPATH, ensure_visible=True, ensure_clickable=True).send_keys(f'{full_name}{number_aleatory}')

        # clica em próximo
        bot.find_element("//span[text()='Próxima']", By.XPATH, ensure_visible=True, ensure_clickable=True).click()

        # validar carregamento da próxima página:
        if not bot.find_element("//input[@name='Passwd']", By.XPATH, ensure_visible=True, ensure_clickable=True, waiting_time=30000):  # espera até 30 segundos
            raise Exception("Falha ao carregar a proxima pagina")

    except Exception as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        raise ValueError(str(error), exc_traceback.tb_lineno, exc_traceback.tb_frame.f_code.co_name)


def account_password(bot: WebBot, password: str):

    try:

        # Digita a senha
        bot.find_element("//input[@name='Passwd']", By.XPATH, ensure_visible=True, ensure_clickable=True).send_keys(password)
        bot.wait(10000)

        # Confirma a senha
        bot.find_element("//input[@name='PasswdAgain']", By.XPATH, ensure_visible=True, ensure_clickable=True).send_keys(password)

        # clica em próximo
        bot.find_element("//span[text()='Próxima']", By.XPATH, ensure_visible=True, ensure_clickable=True).click()

        # TODO: Colocar uma validação para verificar se a senha é forte o suficiente

        # validar carregamento da próxima página:
        if not bot.find_element("//input[@id='phoneNumberId']", By.XPATH, ensure_visible=True, ensure_clickable=True, waiting_time=30000):  # espera até 30 segundos
            raise Exception("Falha ao carregar a proxima pagina")

    except Exception as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        raise ValueError(str(error), exc_traceback.tb_lineno, exc_traceback.tb_frame.f_code.co_name)


def account_phone_verification(bot, telefone):

        try:
            # Digita o telefone
            bot.find_element("//input[@id='phoneNumberId']", By.XPATH, ensure_visible=True, ensure_clickable=True).send_keys(telefone)

            # clica em próximo
            bot.find_element("//span[text()='Próxima']", By.XPATH, ensure_visible=True, ensure_clickable=True).click()

            # validar carregamento da próxima página:
            if not bot.find_element("//input[@id='code']", By.XPATH, ensure_visible=True, ensure_clickable=True, waiting_time=30000):  # espera até 30 segundos
                raise Exception("Falha ao carregar a proxima pagina")

            # TODO: Implementar a verificação do código de verificação via API de SMS

        except Exception as error:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            raise ValueError(str(error), exc_traceback.tb_lineno, exc_traceback.tb_frame.f_code.co_name)
