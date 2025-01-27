
# Framework Libs
from botcity.web import WebBot
from botcity.maestro import *

# System Libs
import os

# local libs
import gmail
import config

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    resources_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
    # maestro.login()

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

                # # Preencher o formulário com o nome e sobrenome
                # gmail.account_input_name(bot, full_name)
                #
                # # Preencher o formulário com a idade e gênero
                # gmail.account_input_age_gender(bot, "Homem")
                #
                # # Preencher o formulário com o nome de usuário
                # gmail.account_username(bot, full_name)
                #
                # # Preencher o formulário com a senha
                # gmail.account_password(bot, "HomeSwiFi@01983355")
                #
                # # Preencher o formulário com o número de telefone e codigo de verificação
                # gmail.account_phone_verification(bot, "")
                #
                # ...

                # Envia status = 'Sucesso' para a BotMaestro
                maestro.finish_task(task_id=execution.task_id,
                                    status=AutomationTaskFinishStatus.SUCCESS,
                                    message="Execução finalizada com sucesso!")
            except Exception as error:
                error_message, error_line, task_name = eval(str(error))
                print(f'{error_message} \n Error line number:{error_line} \n Task Name: {task_name}')
                ...

    except Exception as error:
        error_message, error_line, task_name = eval(str(error))
        print(f'Error Message: {error_message} \n Error line number:{error_line} \n Task Name: {task_name}')
        ...

        # Envia alerta de erro. Usado para notificação via e-mail
        maestro.alert(task_id=execution.task_id,
                      title=config.RPA_FULL_NAME,
                      message=f"f'{error_message} Error line number:{error_line} Task Name: {task_name}'",
                      alert_type=AlertType.ERROR)

        # Envia status = 'Sucesso' para a BotMaestro
        maestro.finish_task(task_id=execution.task_id,
                            status=AutomationTaskFinishStatus.FAILED,
                            message="Erro ao executar a tarefa!")

    finally:
        bot.stop_browser()


if __name__ == '__main__':
    main()
