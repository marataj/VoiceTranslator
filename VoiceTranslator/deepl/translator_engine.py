import requests
from enum import Enum


available_languages={
    "Polski": "PL",
    "English": "EN"
}




class TextTranslated:
    def __init__(self, source_text: str, source_language: str, target_language: str, translated_text: str) -> None:
        self.source_text = source_text
        self.source_language = source_language
        self.target_language = target_language
        self.translated_text = translated_text


class Translator:
    def __init__(self, api_key: str ) -> None:
        self.__api_key = api_key

    def translate(self, source_text: str, source_language: str, target_language: str) -> TextTranslated:
        raw_result = requests.get(
            "https://api-free.deepl.com/v2/translate",
            params={
                "auth_key": self.__api_key,
                "target_lang": target_language,
                "text": source_text,
                "source_lang": source_language
            },
        )

        return TextTranslated(source_text, source_language, target_language, raw_result.json()['translations'][0]['text'])
