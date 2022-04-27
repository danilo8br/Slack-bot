# OBS: Webhooks só serve para postar mensagens externas.

# Importando a biblitoeca Webhook do Slack para enviar mensagens externas.
from slack_sdk.webhook import WebhookClient
# Importando a bibliteoca datetime para enviar data e hora para o Slack.
from datetime import datetime
# Importando a biblioteca de emoji para personalizar as notificações.
import emoji 


# Função para enviar mensagens para o canal "alerts-teste-dan".
def send_message(url):
    '''
    param url: vai receber a url webhook do app foi criado
    ''' 
    webhook = WebhookClient(url)
    data_hora = datetime.today().strftime(' Data: %Y/%m/%d\n Hora: %H:%M:%S') 
    emoji_alerta = emoji.emojize(':warning:')
    emoji_sucesso = emoji.emojize(':white_check_mark:')
    emoji_circulo_amarelo = emoji.emojize(':yellow_circle:')
    mensagem = f'{emoji_circulo_amarelo} - Alerta'

    response = webhook.send(text=mensagem)
    assert response.status_code == 200

# Passando a URL que foi criado no app
send_message("")



#====================================================================================================
# Pegando os parametros em um arquivo json
#====================================================================================================


# Importando a biblitoeca Webhook do Slack para enviar mensagens externas.
from slack_sdk.webhook import WebhookClient
# Importando a biblioteca de emoji para personalizar as notificações.
import emoji
# Import json
import json

# Função para enviar mensagens para o canal "alerts-teste-dan".
def send_message():

    with open('param.json', encoding='utf-8') as file:
        dados_json = json.load(file)

    webhook = WebhookClient(dados_json['url'])
    response = webhook.send(text=dados_json['mensagem'])
    assert response.status_code == 200


send_message()
