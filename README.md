# VoiceTranslator

## **Introduction**

**This project is an simple translator app, created using Python and Django. The main assumption was to enable the speech capture and recognition.**

The VoiceTranslator alows you to translate the standard typed text, and the speech captured with the microphone.

![1](https://user-images.githubusercontent.com/96992545/216851403-6b70707a-0e4c-4b44-96c7-6e59b98b9b09.gif)

![2](https://user-images.githubusercontent.com/96992545/216851408-5b6b646f-0eed-481e-a61b-d923ddd2b264.gif)

The application also allows users to register and log in. Each translation is saved in the integrated database, thanks to which the logged-in user has access to the history of his translations.

![screen-recording (4)](https://user-images.githubusercontent.com/96992545/216851545-20c99a9b-0a9d-4dc3-8e88-54ec66fad10e.gif)

![screen-recording (5)](https://user-images.githubusercontent.com/96992545/216851553-e35695c5-d9d3-48d1-a465-5141d41e503d.gif)

The application works based on the translation engine API - [deepl](https://www.deepl.com/), and the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) package.

The project has been created and tested using Python 3.10.7

The main goal of creating this project was to develop skills related to Django, and the audio recorder feature.

## **Setting up the environment**

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the required libraries.

```bash
pip install -r requirements.txt
```

Add the `.env` file to the `VoiceTranslator/VoiceTranslator` directory. The structure of the `.env` file:

```
SECRET_KEY=""
DEEPL_API_KEY=""
TEMP_DIR=""
DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
DB_PORT=""
```

The instance of postgresql database is required - in order to establish connection, please fill all the `DB_...` variables in the `.env` file accordingly to your DB instance.

Call the instructions below in order to prepare the database structure and load the supported languages.

```bash
python manage.py makemigrations translator
python manage.py migrate
python manage.py set_languages
```

Your environment is ready to use!

## **Contributing**

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## **License**

[MIT](https://choosealicense.com/licenses/mit/)
