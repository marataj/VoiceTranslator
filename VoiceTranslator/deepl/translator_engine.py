from dataclasses import dataclass
from enum import Enum
import os

import requests

__all__ = ["TextTranslated, Translator, SpeechRecognizer"]


@dataclass
class TextTranslated:
    """
    Data class that represents dataset used to single translation.

    """

    source_text: str
    source_language: str
    target_language: str
    translated_text: str


class Translator:
    """
    Class that handles the translation process.

    """

    API_KEY = str(os.getenv("DEEPL_API_KEY"))
    API_ENDPOINT = "https://api-free.deepl.com/v2/translate"

    @classmethod
    def translate(
        cls, source_text: str, source_language: str, target_language: str
    ) -> TextTranslated:
        """
        Function that handles the translation process

        Parameters
        ----------
        source_text : str
            Text to be translated.
        source_language : str
            The source language.
        target_language : str
            The targed language.

        Returns
        -------
        TextTranslated
            Dataset containing data about translated text.

        """
        raw_result = requests.get(
            cls.API_ENDPOINT,
            params={
                "auth_key": cls.API_KEY,
                "target_lang": target_language,
                "text": source_text,
                "source_lang": source_language,
            },
        )

        return TextTranslated(
            source_text,
            source_language,
            target_language,
            raw_result.json()["translations"][0]["text"],
        )
