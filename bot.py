
# Framework Libs
from botcity.web import WebBot
from botcity.maestro import *

# System Libs
import os

# local libs
import gmail


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    resources_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False


    try:

        # Irei consumir os dados de um arquivo CSV
        candidates = gmail.read_csv(fr'{resources_folder}\candidatos.csv')

        # Para Cada linha do CSV (corresponde a um candidato) irei criar uma conta no Gmail
        for index, row in candidates.iterrows():

            try:
                full_name = candidates.iloc[index, 0]

                # Navegador até o site de criar conta do Gmail
                gmail.open_google(bot)

                # Preencher o formulário com o nome e sobrenome
                gmail.account_input_name(bot, full_name)

                gmail.account_input_age_gender(bot, "Homem")

                gmail.account_username(bot, full_name)
                ...
            except Exception as error:
                error_message, error_line, task_name = eval(str(error))
                print(f'{error_message} \n Error line number:{error_line} \n Task Name: {task_name}')
                ...

    except Exception as error:
        error_message, error_line, task_name = eval(str(error))
        print(f'Error Message: {error_message} \n Error line number:{error_line} \n Task Name: {task_name}')
        ...
    finally:
        bot.stop_browser()


if __name__ == '__main__':
    main()
