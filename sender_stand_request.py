import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,\
                         #подставляем url и ручку создания пользователя
                         json=body, headers=data.headers) #подставляем тело запроса и хедеры

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS_PATH, \
                         # подставляем url и ручку создания набора
                         json=kit_body, headers=data.authorization)#вместе с телом подставляем хедеры созданных пользователем




