import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',authenticator=authenticator)

language_translator.set_service_url(url)
languages = language_translator.list_languages().get_result()

def englishtofrench(englishtext):
    frenchtranslation = language_translator.translate(
        text=englishtext, model_id="en-fr").get_result()
    return frenchtranslation['translations'][0]['translation']

def frenchtoenglish(frenchtext):
    englishtranslation = language_translator.translate(
        text=frenchtext, model_id="fr-en").get_result()
    return englishtranslation['translations'][0]['translation']