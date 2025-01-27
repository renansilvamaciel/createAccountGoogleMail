from botcity.maestro import BotMaestroSDK
import os


MAESTRO_KEY = os.getenv("MAESTRO_KEY")
MAESTRO_LOGIN = os.getenv("MAESTRO_LOGIN")
MAESTRO_SERVER = os.getenv("MAESTRO_SERVER")
maestro = BotMaestroSDK()
# maestro.login(MAESTRO_SERVER, MAESTRO_LOGIN, MAESTRO_KEY)

RPA_FULL_NAME = "RPA_CREATE_ACCOUNT_GOOGLE"

# maestro.login(server="https://developers.botcity.dev", login="0180fbc5-05f0-4bd9-9e14-e89c1ab230ad", key="018_JJTH45IDOCBDMIEZDAGA")

