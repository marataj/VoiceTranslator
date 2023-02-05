# VoiceTranslator


## **Introduction**

**This project is an simple translator app, created using Python and Django. The main assumption was to enable the speech capture and recognition.**

The VoiceTranslator alows you to translate the standard typed text, and the speech captured with the microphone.

[gif] [gif]

The application also allows users to register and log in. Each translation is saved in the integrated database, thanks to which the logged-in user has access to the history of his translations.

[gif] [gif]

The application works based on the translation engine API - [deepl](https://www.deepl.com/), and the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) package.

The project has been created and tested using Python 3.10.7

The main goal of creating this project was to develop skills related to Django, and the audio recorder feature.

## **Setting up the environment**

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the required libraries.

```bash
pip install -r requirements.txt
```
Add the `.env` file to the `VoiceTranslator/VoiceTranslator` directory. The structure of the  `.env` file:
```
SECRET_KEY=""
DEEPL_API_KEY=""
TEMP_DIR=""
```

## **Contributing**

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## **License**

[MIT](https://choosealicense.com/licenses/mit/)