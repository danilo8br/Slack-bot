# Enviando arquivos para o Slack utlizando Bot

# ============================================
# pip install slackclient, pip install dotenv
# ============================================

# Importando a biblioteca do Slack.
import slack
# Importando a blioteca de sistema operacional.
import os
# Importando a biblioteca pathlib para trabalhar com arquivos e diretórios.
from pathlib import Path
# Importando a biblioteca dotenv para carregar o arquivo de variavel de ambiente.
from dotenv import load_dotenv

def bot_file(canal_slack, arquivo):
    '''
    param canal_slack: vai receber o canal do Slack para enviar os arquivos
    param arquivo: vai receber o arquivo que vai ser enviado
    '''
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

    client.files_upload(channels=canal_slack, file=arquivo)

bot_file('#testenovo', 'Arquivos_teste/Figure_1.png')


